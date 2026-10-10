# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A searchable knowledge base for *Wraith: The Oblivion*, not a software project: there is no build, lint or test suite. Two book bundles (`wraith-20th-anniversary/`, `dark-kingdom-of-jade/`) each hold a thematic `book_index.md`, a SQLite FTS5 `book_chunks.db` and a copy of `scripts/query_chunks.py`. The top level adds `library_index.md` (cross-book synthesis) and `scripts/query_library.py` (search several databases at once). `README.md` and the per-book `README.md` files explain usage; the notes below are what they don't.

## Answering questions

- Start with the book's `book_index.md` (WR20's is ~100 KB: read its header and the relevant chapter), then query the database for exact numbers, quotes and page checks. For anything about Jade, read `library_index.md` first.
- Run Python as `py -3 ...` on this Windows machine (`python` is not a real interpreter here). Standard library only.
- Canon policy: **WR20 (20th Anniversary Edition) is the core and wins conflicts.** *Dark Kingdom of Jade* is a 1995 book for an earlier edition, so small inconsistencies are expected; record them in `library_index.md` rather than silently picking one. DKoJ is also meant as crossover material for a *Kindred of the East* chronicle; neither book mentions that line, so keep any such material labeled as suggestion.
- Cite **printed** page numbers. The databases store `page` (PDF page) and `printed_page`. WR20: printed = PDF − 65 (Prologue is roman numerals, PDF 2–65). DKoJ: printed = PDF − 2. The indexes and the books' own indexes use printed pages.

## Querying

```bash
py -3 wraith-20th-anniversary/scripts/query_chunks.py wraith-20th-anniversary/book_chunks.db "Skinride" --chapter "Chapter 5:" --brief
py -3 wraith-20th-anniversary/scripts/query_chunks.py wraith-20th-anniversary/book_chunks.db --printed 236
py -3 scripts/query_library.py wraith-20th-anniversary/book_chunks.db dark-kingdom-of-jade/book_chunks.db "Immortal Guard" --brief
```

- `--chapter` matches the chapter tag; `--section` matches only the breadcrumb after the chapter. Both are substrings, so write `"Chapter 1:"` with the colon or it also matches Chapters 10–13. WR20 tags are `Chapter N: Title`; DKoJ tags are spelled out (`Chapter Eight: ...`).
- Schema: `chunks(chunk_id, page, chapter, section, text, printed_page)` plus FTS5 table `chunks_fts` (porter). Invalid FTS syntax (e.g. `p'o`) is retried with each word quoted.
- A name that appears in WR20's own Index (printed pp. 491–509) can rank that chunk first; add `--chapter` to skip it.

## Editing rules and gotchas

- `wraith-20th-anniversary/scripts/query_chunks.py` and `dark-kingdom-of-jade/scripts/query_chunks.py` must stay byte-identical (check with `cmp`). Edit one, copy to the other. They differ from the book-indexer skill's stock script (printed pages, section paths, `--printed`, `--section`, quote-tolerant filters).
- The databases were built from PDFs that are **not** in the repo (`C:\Users\Vivek\Documents\World of Darkness\Wraith\`) with a custom PyMuPDF extractor that was kept outside the repo. The extraction and tagging code is not recoverable from here, so treat the `.db` files as artifacts. Do not rebuild them with the skill's stock `pdftotext` flow: it would lose column ordering, printed pages and bookmark-derived section breadcrumbs.
- Page citations in the indexes were checked against the databases. After editing an index, check new cites with a query (`--printed N`) rather than from memory.
- Keep the structure of each bundle (`book_index.md`, `book_chunks.db`, `README.md`, `scripts/query_chunks.py`) intact so a folder can be copied out standalone. The databases contain each book's full extracted text, so the repo should stay private.
- To add a book: create a new slug folder with the same four items, then update `library_index.md` (books list, themes, agreements, disagreements) and the README table and tree.
