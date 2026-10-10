# Wraith: The Oblivion — 20th Anniversary Edition — Searchable Index Bundle

This bundle lets Claude answer questions about *Wraith: The Oblivion — 20th Anniversary Edition* without re-reading the original PDF. **This is the core book of the library** (see the top-level `README.md` and `library_index.md`).

## Files

- **`book_index.md`** — thematic index: chapter-by-chapter summaries, rules numbers, the full table of the 16 Guilds and their 160 arts, page map, cross-cutting themes, glossary, and notes on how each chapter relates to *Dark Kingdom of Jade*. About 100 KB; read the header and page map first, then the chapters you need (each chapter is a self-contained `##` section).
- **`book_chunks.db`** — SQLite database of 7,122 paragraph-level chunks with FTS5 full-text search. Every chunk is tagged with its PDF page, printed page, chapter and a section breadcrumb. Query it; don't load it.
- **`scripts/query_chunks.py`** — command-line helper for querying the database.

Book: *Wraith: The Oblivion — 20th Anniversary Edition* (White Wolf / Onyx Path, 2018), 594 PDF pages, indexed 2026-10-10.

## Page numbers (important)

- The database column `page` is the **PDF page**. The column `printed_page` is the number printed on the page, which is what the book's own Index and table of contents use and what `book_index.md` cites.
- For PDF pages 66–593: **printed = PDF − 65** (printed p. 125 = PDF p. 190). The Prologue (PDF pp. 2–65) uses roman numerals i–lxiv; the back cover has no printed number.
- Look up a printed page with `--printed N`. Search results show both numbers, plus the chapter and section path.

## For a future Claude session: how to use this bundle

1. Read the top of `book_index.md` (How to use, Map of the book, Where to look), then the chapter section that matches the question. Broad and thematic questions are mostly answerable from it.
2. For precise facts, exact numbers (dice pools, costs, difficulties) or quote verification, query the chunk database (use `py -3` on Windows, `python3` elsewhere):

   ```bash
   python3 scripts/query_chunks.py book_chunks.db "Skinride"
   python3 scripts/query_chunks.py book_chunks.db "Catharsis AND Eidolon" --chapter "Chapter 6:"
   python3 scripts/query_chunks.py book_chunks.db --printed 236
   python3 scripts/query_chunks.py book_chunks.db --section "Puppeteers"
   python3 scripts/query_chunks.py book_chunks.db "Immortal Guard" --brief
   ```

   - Full-text search supports phrase queries (`"exact phrase"`), `AND`/`OR`/`NOT`, and prefix matching (`harrow*`). If a query isn't valid FTS5 syntax (for example `p'o`), the script retries with each word quoted.
   - `--chapter` matches the chapter tag and `--section` matches only the part of the breadcrumb after the chapter. Both are substring matches. **Include the colon** (`"Chapter 1:"`), or "Chapter 1" also matches Chapters 10–13.
   - Every one of the 160 Arcanoi arts has its own section in Chapter 5, e.g. `--section "Master's Voice"` (straight and curly apostrophes are treated alike).
   - Names that appear in the book's own Index (printed pp. 491–509) can rank that Index chunk first; add `--chapter "Chapter 13:"` (or the relevant chapter) to skip it.
3. Cite printed page numbers when quoting or referencing facts.
4. Only fall back to the original PDF for things text extraction can't capture: art, maps, tables whose layout matters, character sheets.

## Chapter tags in the database

`Prologue: The Face of Death` · `Credits` · `Table of Contents` · `Chapter 1: Introduction` · `Chapter 2: Setting` · `Chapter 3: Rules` · `Chapter 4: Character` · `Chapter 5: Traits` · `Chapter 6: The Shadow` · `Chapter 7: Storytelling` · `Chapter 8: Systems` · `Chapter 9: Drama` · `Chapter 10: Spectres` · `Chapter 11: The Risen` · `Chapter 12: The World of Darkness` · `Chapter 13: The Other Dark Kingdoms` · `Appendix: Orpheus` · `Index` · `Testimonials` · `Kickstarter Backers` · `Character Sheet` · `Shadow Sheets` · `Back Cover`. Section breadcrumbs come from the PDF's own bookmarks (1,311 of them), so they are accurate down to individual Arcanoi powers and Spectre/plasmic stat blocks.

## Known extraction caveats

- **Illustrated pages** (much of the Prologue, chapter openers, the back cover) have little or no text layer; there is no OCR.
- **Drop caps:** the first letter of some paragraphs is a graphic and is missing from the text (for example "ow does…" for "How does…"). Search for a word's remainder, or use a phrase that doesn't start at the first word.
- **Sidebars** can interleave with body text when a column is cut, and hyphenated words are rejoined by dictionary, so a rare word may keep a stray hyphen.
- **The book's Index** (printed pp. 491–509) is included as text and can be searched, but its page numbers are printed pages.
- The character sheet and Shadow sheets contain only field labels.

## Scope note

The chunk database holds the **extracted text of the whole book** split into paragraphs. It is a research aid for someone who owns the book; keep the repository private and don't redistribute the database.
