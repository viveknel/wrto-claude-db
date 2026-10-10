# wrto-claude-db — Wraith: The Oblivion Searchable Library

My *Wraith: The Oblivion* database for use with Claude. It is a searchable index of two sourcebooks, built so that questions can be answered without re-reading the original PDFs. Each book has its own self-contained bundle (a thematic index plus a full-text search database), and a top-level synthesis layer ties them together.

**The core of this library is *Wraith: The Oblivion — 20th Anniversary Edition*.** Everything else is measured against it.

Built with Anthropic's book-indexer skill (the PDFs were extracted once, the text was tagged by chapter and section, and a thematic index and a queryable chunk database were written from it).

## Before you use this: the books are not one continuity

- **`wraith-20th-anniversary/`** is the **core canon**: the 2018 rebuild of the game. Use it for rules, setting and terminology.
- **`dark-kingdom-of-jade/`** was written in 1995 for an **earlier edition** of *Wraith: The Oblivion*. It is the detailed guide to the Chinese afterlife (the Jade Kingdom of Qin Shihuang / Yu Huang). Because it predates the 20th Anniversary Edition, **expect minor inconsistencies** with the core book (the Arcanoi format, how the p'o relates to the Shadow, a few numbers, dates and names). When the two disagree, the 20th Anniversary Edition wins. `library_index.md` lists the differences and suggests rulings.
- *Dark Kingdom of Jade* can also be used as **crossover material for a *Kindred of the East* chronicle**. Neither book in this library mentions Kindred of the East, so `library_index.md` gives suggestions rather than canon.
- The 20th Anniversary Edition has its own short Jade chapter (Chapter 13) that agrees with the 1995 book on the main facts. The 1995 book has far more detail.

## What's in here

| Book | Folder | Pages | Role |
|---|---|---|---|
| *Wraith: The Oblivion — 20th Anniversary Edition* (White Wolf / Onyx Path, 2018) | `wraith-20th-anniversary/` | 594 | Core |
| *Wraith: The Oblivion — The Dark Kingdom of Jade* (White Wolf, 1995, WW6010) | `dark-kingdom-of-jade/` | 138 | Supplement, earlier edition, Kindred of the East crossover |

```
.
├── README.md                  ← you are here
├── library_index.md           ← cross-book synthesis: themes, agreements,
│                                disagreements, conversion notes,
│                                Kindred of the East suggestions
├── scripts/
│   └── query_library.py       ← search both databases at once
├── wraith-20th-anniversary/
│   ├── book_index.md          ← thematic index (read this for broad questions)
│   ├── book_chunks.db         ← full-text search database (exact facts/quotes)
│   ├── README.md              ← usage notes for this book's bundle
│   └── scripts/
│       └── query_chunks.py    ← search this book's database alone
└── dark-kingdom-of-jade/
    ├── book_index.md
    ├── book_chunks.db
    ├── README.md
    └── scripts/
        └── query_chunks.py
```

Each book folder is a complete, self-contained bundle: either one can be copied out and used on its own.

## Quick start

**Broad or thematic question about one book:** read that book's `book_index.md`. The 20th Anniversary index is long (about 100 KB), so read its header and page map and then the chapter you need. The Jade index is about 47 KB.

**Exact quote, precise fact or page lookup:** query that book's database (use `py -3` on Windows, `python3` elsewhere):

```bash
python3 wraith-20th-anniversary/scripts/query_chunks.py wraith-20th-anniversary/book_chunks.db "Skinride"
python3 wraith-20th-anniversary/scripts/query_chunks.py wraith-20th-anniversary/book_chunks.db --printed 236
python3 wraith-20th-anniversary/scripts/query_chunks.py wraith-20th-anniversary/book_chunks.db "Angst" --chapter "Chapter 6:"
python3 dark-kingdom-of-jade/scripts/query_chunks.py dark-kingdom-of-jade/book_chunks.db "Immortal Guard" --brief
python3 dark-kingdom-of-jade/scripts/query_chunks.py dark-kingdom-of-jade/book_chunks.db "Mrs. Meng" --chapter "Guided Tour"
```

**A question that spans both books:** read `library_index.md` first, then search both:

```bash
python3 scripts/query_library.py wraith-20th-anniversary/book_chunks.db dark-kingdom-of-jade/book_chunks.db "Chains of the Emperor" --brief
```

Full-text search supports phrase queries (`"exact phrase"`), `AND`/`OR`/`NOT`, and prefix matching (`harrow*`). Queries that are not valid search syntax (for example `p'o`) are retried with each word quoted.

**Page numbers.** Results show both the **PDF page** and the **printed page**. The indexes cite printed pages. For the 20th Anniversary book, printed = PDF − 65 (Prologue pages use roman numerals); for *Dark Kingdom of Jade*, printed = PDF − 2. `--printed N` looks up a printed page. `--chapter` and `--section` match substrings, so include the colon in `"Chapter 1:"` or it also matches Chapters 10–13.

## Requirements

Python 3 with the standard library only (`sqlite3` is built in; no packages to install).

## Notes on scope

- The chunk databases hold the **extracted text of each whole book**, split into paragraphs. They are a research aid for someone who owns the books; keep this repository private and don't redistribute the databases.
- The original PDFs are not in the repository. Text extraction has a few known limits (art pages have no text, some drop-cap letters are missing, sidebars can interleave with body text); each book's `README.md` lists them.
- Mechanically dense chapters (the Arcanoi, stat blocks, equipment) are summarized or tabulated in the indexes and are best queried from the databases directly.
- The query scripts differ slightly from the book-indexer skill's stock versions: the databases have an extra `printed_page` column, results show chapter and section paths, and `--printed` / `--section` options were added.
- Where the books disagree, `library_index.md` says so explicitly rather than silently picking one.

## Adding another book later

Add the new PDF's bundle as a new folder (for example `wraith-<slug>/`) built the same way, then update `library_index.md` (books list, themes, agreements, disagreements) and this README's table and tree. A natural next step would be other *Wraith* "Dark Kingdoms" or Stygia sourcebooks, with the same rule: the 20th Anniversary Edition stays the baseline, and anything older is checked against it.
