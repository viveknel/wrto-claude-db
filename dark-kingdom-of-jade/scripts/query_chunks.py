#!/usr/bin/env python3
"""
query_chunks.py — Query a book_chunks.db built by build_chunk_db.py.

Usage:
    python query_chunks.py DB_PATH "search terms"                    # full-text search
    python query_chunks.py DB_PATH "search terms" --chapter "Chapter 5:"   # search inside one chapter
    python query_chunks.py DB_PATH "search terms" --section "Harrowing"    # ...or one section
    python query_chunks.py DB_PATH --page 42                          # dump one PDF page
    python query_chunks.py DB_PATH --printed 17                       # dump one PRINTED page (the number in the book/its index)
    python query_chunks.py DB_PATH --range 40 45                      # dump a PDF page range
    python query_chunks.py DB_PATH --chapter "Chapter 3:"             # every chunk in a chapter
    python query_chunks.py DB_PATH --section "Fatalism"               # every chunk whose section path contains the text

Full-text search uses SQLite FTS5 (supports AND/OR/NOT, "phrase queries",
and prefix* matching). Results are ranked by relevance. If a query is not
valid FTS5 syntax (e.g. p'o or a stray hyphen) it is retried with each word
quoted. Each hit is labelled with its PDF page, its printed page (when the
page has one), its chapter and its section path, for citation.

--chapter / --section are substring matches (curly and straight apostrophes are
treated alike): include the colon ("Chapter 1:")
or "Chapter 1" will also match Chapters 10-13. --brief truncates each chunk.
"""

import argparse
import re
import sqlite3
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def columns(conn):
    return {r[1] for r in conn.execute("PRAGMA table_info(chunks)")}


def select_list(cols):
    printed = "c.printed_page" if "printed_page" in cols else "NULL"
    section = "c.section" if "section" in cols else "NULL"
    return f"c.page, {printed} AS printed, c.chapter, {section} AS section, c.text"


def filters(cols, chapter, section, printed=None):
    where, params = [], []
    # Curly and straight quotes/apostrophes are treated as the same character
    # so --section "Master's Voice" matches the book's "Master’s Voice".
    def fold(x):
        return x.replace("’", "'").replace("‘", "'")
    sql_fold = "REPLACE(REPLACE({0}, char(8217), char(39)), char(8216), char(39))"
    if chapter:
        where.append(sql_fold.format("c.chapter") + " LIKE ?")
        params.append(f"%{fold(chapter)}%")
    if section and "section" in cols:
        where.append(sql_fold.format("c.section") + " LIKE ?")
        params.append(f"%{fold(section)}%")
    if printed is not None and "printed_page" in cols:
        where.append("c.printed_page = ?")
        params.append(str(printed))
    return where, params


def quote_terms(query):
    toks = re.findall(r"[^\s\"]+", query)
    return " ".join('"' + t.replace('"', "") + '"' for t in toks)


def search(conn, query, limit, chapter, section):
    cols = columns(conn)
    where, params = filters(cols, chapter, section)
    sql = f"""
        SELECT {select_list(cols)}, bm25(chunks_fts) AS rank
        FROM chunks_fts
        JOIN chunks c ON c.chunk_id = chunks_fts.rowid
        WHERE chunks_fts MATCH ? {''.join(' AND ' + w for w in where)}
        ORDER BY rank
        LIMIT ?
    """
    try:
        return conn.execute(sql, [query, *params, limit]).fetchall()
    except sqlite3.OperationalError:
        return conn.execute(sql, [quote_terms(query), *params, limit]).fetchall()


def listing(conn, where, params):
    cols = columns(conn)
    sql = f"SELECT {select_list(cols)} FROM chunks c"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY c.chunk_id"
    return conn.execute(sql, params).fetchall()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("db_path")
    ap.add_argument("query", nargs="?", help="Full-text search query")
    ap.add_argument("--page", type=int, help="PDF page number")
    ap.add_argument("--printed", help="printed page number (as shown in the book and its index)")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"), help="PDF page range")
    ap.add_argument("--chapter")
    ap.add_argument("--section")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--brief", action="store_true", help="truncate each chunk to ~300 characters")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db_path)
    cols = columns(conn)
    where, params = filters(cols, args.chapter, args.section, args.printed)

    if args.query:
        rows = search(conn, args.query, args.limit, args.chapter, args.section)
    elif args.page is not None:
        rows = listing(conn, ["c.page = ?"] + where, [args.page] + params)
    elif args.range:
        rows = listing(conn, ["c.page BETWEEN ? AND ?"] + where, [args.range[0], args.range[1]] + params)
    elif args.printed is not None or args.chapter or args.section:
        rows = listing(conn, where, params)
    else:
        sys.exit("Provide a search query, --page, --printed, --range, --chapter or --section")

    if not rows:
        print("No results.")
        return

    for row in rows:
        page, printed, chapter, section, text = row[:5]
        label = f"PDF p.{page}"
        if printed:
            label += f" | printed p.{printed}"
        where_ = " > ".join(x for x in (chapter, section) if x)
        print(f"--- {label}" + (f" | {where_}" if where_ else "") + " ---")
        if args.brief and len(text) > 300:
            text = text[:300].rstrip() + " …"
        print(text)
        print()


if __name__ == "__main__":
    main()
