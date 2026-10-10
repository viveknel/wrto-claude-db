# Wraith: The Oblivion — The Dark Kingdom of Jade — Searchable Index Bundle

This bundle lets Claude answer questions about *Wraith: The Oblivion — The Dark Kingdom of Jade* (White Wolf, 1995, product code WW6010) without re-reading the original PDF.

**Edition caution.** This book was written for an **earlier edition** of *Wraith: The Oblivion*. The core of this library is *Wraith: The Oblivion — 20th Anniversary Edition* (`../wraith-20th-anniversary/`), so expect some minor inconsistencies (Arcanoi format, Shadow wording, small timeline and number differences), and treat the 20th Anniversary text as authoritative where they conflict. `../library_index.md` lists the differences. This book is also suitable as **crossover material for a *Kindred of the East* chronicle** (that line is not part of this library).

## Files

- **`book_index.md`** — thematic index: chapter summaries, rules numbers (Martial Arts, Backgrounds, the Ways of the Scholar/Artisan/Farmer/Merchant/Soul, Chains of the Emperor), NPC templates, edition and crossover notes, cross-cutting themes and a glossary. Read it first, in full (about 47 KB).
- **`book_chunks.db`** — SQLite database of 932 paragraph-level chunks with FTS5 full-text search, tagged with PDF page, printed page, chapter and section breadcrumb.
- **`scripts/query_chunks.py`** — command-line helper for querying the database.

Book: *The Dark Kingdom of Jade*, 138 PDF pages, indexed 2026-10-10.

## Page numbers (important)

- `page` in the database is the **PDF page**; `printed_page` is the number printed on the page and used by the book's own contents and by `book_index.md`.
- **Printed = PDF − 2** (printed p. 1 = PDF p. 3). Cover and front matter pages have no printed number.
- Look up a printed page with `--printed N`.

## For a future Claude session: how to use this bundle

1. Read `book_index.md` in full for orientation and thematic answers.
2. For exact figures, stat blocks or quote verification, query the database (use `py -3` on Windows, `python3` elsewhere):

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "Immortal Guard"
   python3 scripts/query_chunks.py book_chunks.db "Filial Duty" --chapter "Chapter Eight"
   python3 scripts/query_chunks.py book_chunks.db --printed 20
   python3 scripts/query_chunks.py book_chunks.db "Mrs. Meng" --chapter "Guided Tour"
   ```

   - Full-text search supports phrase queries, `AND`/`OR`/`NOT` and prefix matching. If a query isn't valid FTS5 syntax (for example `p'o`), the script retries with each word quoted.
   - `--chapter` matches the chapter tag and `--section` matches only the part of the breadcrumb after the chapter (for example `--section "Seven Days"`). Both are substring matches. Chapter tags are spelled out: `Chapter One: The Chinese Dead` through `Chapter Eight: Systems and Stories`, plus `Front Matter`, `Ghost Story: A Prelude to Hell` and `Introduction`.
3. Cite printed page numbers when referencing facts.
4. Only fall back to the original PDF for art, maps, or layout the text layer can't capture.

## Known extraction caveats

- The book is two-column with full-page art; text was reordered column by column and cross-checked, but a few sidebars may interleave with body text.
- The first letter of some paragraphs (a drop cap) is a graphic and is missing from the extracted text.
- Hyphenated words are rejoined by dictionary; rare words can keep a stray hyphen.
- Spelling follows the book: *Qin Shihuang*, *p’o* (typographic apostrophe; a search for `p'o` is retried automatically, and `--section`/`--chapter` treat straight and curly apostrophes alike), *Feng-tu* in this book vs. *Feng Tu* in the 20th Anniversary book.
- Art-only pages and the cover have no text.

## Scope note

The chunk database holds the **extracted text of the whole book** split into paragraphs. It is a research aid for someone who owns the book; keep the repository private and don't redistribute the database.
