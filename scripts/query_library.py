#!/usr/bin/env python3
"""
query_library.py — Full-text search across multiple per-book chunk
databases (each built by build_chunk_db.py) at once.

Use this when you have several single-book bundles (separate per-book
bundles) and want to search across all of them for a cross-book question,
without merging the databases.

Usage:
    python query_library.py book1/book_chunks.db book2/book_chunks.db "search terms"
    python query_library.py */book_chunks.db "search terms" --limit 10

Results are grouped by book (the database's folder name) and ranked within
each book by relevance. This does NOT merge rankings across books — it shows
the top matches per book so you can see which books discuss the topic and
how, side by side. Each hit shows its PDF page, printed page (when the page
has one), chapter and section path. Queries that are not valid FTS5 syntax
(e.g. p'o) are retried with each word quoted. --brief truncates each chunk.
"""

import argparse
import re
import sqlite3
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def quote_terms(query):
    toks = re.findall(r"[^\s\"]+", query)
    return " ".join('"' + t.replace('"', "") + '"' for t in toks)


def search_one(db_path: str, query: str, limit: int):
    conn = sqlite3.connect(db_path)
    cols = {r[1] for r in conn.execute("PRAGMA table_info(chunks)")}
    printed = "c.printed_page" if "printed_page" in cols else "NULL"
    section = "c.section" if "section" in cols else "NULL"
    sql = f"""
        SELECT c.page, {printed}, c.chapter, {section}, c.text, bm25(chunks_fts) AS rank
        FROM chunks_fts
        JOIN chunks c ON c.chunk_id = chunks_fts.rowid
        WHERE chunks_fts MATCH ?
        ORDER BY rank
        LIMIT ?
    """
    try:
        try:
            rows = conn.execute(sql, (query, limit)).fetchall()
        except sqlite3.OperationalError:
            rows = conn.execute(sql, (quote_terms(query), limit)).fetchall()
    except sqlite3.OperationalError as e:
        print(f"  (query error on {db_path}: {e})", file=sys.stderr)
        rows = []
    finally:
        conn.close()
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("db_paths", nargs="+", help="Paths to book_chunks.db files, followed by the query")
    ap.add_argument("--limit", type=int, default=5, help="Max results per book (default 5)")
    ap.add_argument("--brief", action="store_true", help="truncate each chunk to ~300 characters")
    args = ap.parse_args()
    if len(args.db_paths) < 2:
        sys.exit('Usage: query_library.py DB [DB ...] "search terms"')
    *db_paths, query = args.db_paths

    for db_path in db_paths:
        book_label = Path(db_path).resolve().parent.name or Path(db_path).stem
        rows = search_one(db_path, query, args.limit)
        print(f"=== {book_label} ({db_path}) ===")
        if not rows:
            print("  (no matches)")
        for page, printed, chapter, section, text, _rank in rows:
            label = f"PDF p.{page}" + (f" | printed p.{printed}" if printed else "")
            where = " > ".join(x for x in (chapter, section) if x)
            print(f"  --- {label}" + (f" | {where}" if where else "") + " ---")
            if args.brief and len(text) > 300:
                text = text[:300].rstrip() + " …"
            for line in text.strip().splitlines():
                print(f"  {line}")
        print()


if __name__ == "__main__":
    main()
