# Track 2 — Catalog Visualizer 🟢 Safe

**Zone: 🟢 Safe** — it only reads a sample spreadsheet that ships with this folder,
touches nothing shared, and is fully throwaway.

## What you'll build

A visual explorer for `data/catalog.csv` — a sample catalog of ~200 (entirely fictional)
streaming titles with genre, year, rating, and duration. Charts, search, filters:
you decide what "explorer" means. This is the track closest to real office work —
swap in your own CSV later and the same tool works.

## What it teaches

- Turning a **spreadsheet into something visual and interactive**
- How Claude reads and transforms tabular data
- That "build me a dashboard for this file" is a complete, reasonable request

## Your first prompt

Copy this into Claude, then adjust it to taste:

> Look at `tracks/2-csv-visualizer/data/catalog.csv` and tell me what columns it has.
> Then build me a single self-contained `index.html` page inside
> `tracks/2-csv-visualizer/` — plain HTML, CSS, and JavaScript, no frameworks and
> nothing to install — that loads that CSV and shows: a bar chart of titles per genre,
> a chart of titles per release year, and a searchable, sortable table of all titles.
> Draw the charts yourself with HTML/CSS or SVG rather than pulling in a charting
> library. Make a short plan first before writing code.
>
> When it is built, start a local web server in this folder with Python and **open** the
> resulting `http://localhost` page in the browser — it fetches a CSV, which only works
> over http. If a tab is showing this same page from a file path, close that one — it
> cannot load the data — but leave every other tab open, including the workshop guide.

Claude will start a small web server and open the page for you. Check the address bar
says `localhost` — if you are looking at a long file path instead, that is the file
preview, not your running app. See **If you get stuck**.

## Stretch goals (if you finish early)

- Add a filter by rating, or an "average duration by genre" stat
- Ask Claude: "what's the most surprising thing in this dataset?" and chart its answer
- Point the same page at a *different* CSV and see what survives

## If you get stuck

Paste the exact error (or a screenshot) back to Claude.

**"Could not load data/catalog.csv"**, or a blank page — the most common one, and it is
not your fault. The page is being opened as a file instead of through a web address. Look
at the address bar: a long `/Users/...` path is the problem; `localhost` is what you want.
Say *start a web server in this folder and open the localhost page in the browser*.

**Two tabs with the same name?** Desktop previews the file it just wrote *as well as* the
served page, and it may land you on the broken one. Two ways to tell them apart: the
working tab says `localhost` in the address bar, and Claude's message includes a card
reading **"localhost:… · Opened in Browser"** with an **Open** button — that button always
goes to the working version. If the stale tab is still cluttering things up, say *close
the tab showing this page as a local file* and Claude will close it for you. You may also see an orange warning that a tab
"shows a single file and can't follow links" — that is the same preview tab, and it goes
away when the tab does.

**Stuck for 10 minutes? Grab a facilitator.**

## Could you ship this? (Part 5 preview)

Yes, as long as it stays static and the data isn't sensitive. A page plus a CSV deploys
anywhere static files go. The moment the CSV becomes *company* data, you've left the
🟢 Safe zone — that's a Review conversation, not a blocker.
