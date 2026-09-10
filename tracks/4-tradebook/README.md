# Track 4 — Tradebook 🟢 Safe to build · 🔴 Stop to ship

**Zone: Safe to build · Stop to ship** — as a workshop exercise on the fake data in this
folder, it's perfectly safe. The red half of the label is the lesson: what you'll build
*looks* like a production trading tool, and that resemblance is exactly why nothing like
it should ever be wired to real financial data or shared systems without engineering.
Build it, enjoy it, and notice how production-ish it feels — that feeling is the warning.

## What you'll build

A trading-desk-style blotter over `data/trades.csv` — ~150 entirely synthetic trades in
made-up instruments (you'll notice the tickers are things like `ZORP` and `QUUX`; nothing
here resembles a real security). Start with a table and summary stats, then grow it into
a mini terminal: filters, per-instrument views, a form to add a hypothetical trade.

## What it teaches

- **Progressive complexity** — start with a table, keep adding until it feels like a product
- Computing summaries (totals, per-instrument breakdowns) from raw rows
- Where the line is between "impressive demo" and "production system"

## Your first prompt

Copy this into Claude, then adjust it to taste:

> Look at `tracks/4-tradebook/data/trades.csv` and describe its columns. Then build a
> trading-blotter web page inside `tracks/4-tradebook/` using **only Python's standard
> library — `http.server` and `sqlite3`, no pip installs, no frameworks** — for the
> backend, plus plain HTML, CSS, and JavaScript, no frameworks and nothing to install,
> for the page itself. Load the CSV into a local SQLite database once, then serve
> trades to the page as JSON from a small `/api/trades` route — a plain static-file
> server can't do that part, so write a small Python server for it. Dark background,
> dense layout, like a trading terminal. Show: summary stats at the top (total trades,
> total notional buys vs sells), a per-instrument breakdown, and a sortable, filterable
> table of all trades. Make a short plan first before writing code.
>
> When it is built, start the server in this folder and **open** the resulting
> `http://localhost` page in the browser — the page needs that `/api/trades` route, so
> it won't work opened as a file. If a tab is showing this same page from a file path,
> close that one — it can't reach the data that way — but leave every other tab open,
> including the workshop guide.

## Stretch goals (if you finish early)

- Add a form to enter a new hypothetical trade (it can just update the page — no need
  to save it)
- Add a "biggest trades today" panel
- Ask Claude: "what would this need to become a real tool the trading desk could use?"
  — and read the answer through the 🔴 Stop lens

## If you get stuck

Paste the exact error (or a screenshot) back to Claude and ask it to fix it.

**Blank page, or the table never loads** — the most common one, and it is not your fault.
Usually the page is being opened as a file instead of through a web address. Look at the
address bar: a long `/Users/...` or `C:\...` path is the problem; `localhost` is what you
want. Say *start the server in this folder and open the localhost page in the browser*.

**"address already in use"** — a port conflict, same as any local server. Tell Claude and
it'll pick another port or stop the old process.

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

**No — full stop, and that's the point of this track.** Real trade data, real prices,
anything anyone would make a decision from: that's authenticated internal data, shared
systems, and audit requirements. The static page you built is harmless; the *idea* of it
in production is an engineering project with compliance in the room. Knowing that
difference on sight is the most valuable thing this track teaches.
