# Track 3 — Personal Notes App 🟡 Review

**Zone: 🟡 Review** — not because notes are risky, but because of *how it runs*: this is
a real application with a running process and its own database. It only affects you
today, but anything built this way that other people would rely on needs a review
conversation before it leaves your machine.

## What you'll build

A personal notes app that actually works like an app: create a note, see your list,
edit, delete — and the notes are still there after you stop and restart it, because
they live in a real database file on your machine. No sample data needed; you'll write
your own notes.

## What it teaches

- What a **running local service** is — start it, use it, stop it, restart it
- Full **create / read / update / delete** against a real database (SQLite)
- Why this kind of app is different from a static page — and why that difference is
  exactly where the shipping boundary sits

## Your first prompt

Copy this into Claude, then adjust it to taste:

> Build me a personal notes app inside `tracks/3-notes-app/` using **only Python's
> standard library — `http.server` and `sqlite3`, no pip installs, no frameworks**.
> One `app.py` file that
> serves a simple web page where I can create a note with a title and body, see all my
> notes newest-first, edit a note, and delete one. Store the notes in a local SQLite
> file so they survive a restart. **Do not use pop-up dialogs — no `confirm()` or
> `alert()`.** They do not appear in Claude Code's built-in browser, so a Delete button
> wired to one does nothing at all. If you want an "are you sure?" step before deleting,
> put it inline on the page instead. Make a short plan first before writing code, then run
> it and **open** the resulting `http://localhost` page in the browser.

## Try this once it runs

1. Create two or three notes.
2. Ask Claude to **stop the server** — refresh the browser and watch the page die.
   That's what "the app isn't running" looks like.
3. Ask Claude to **start it again** — your notes are still there. That's the database.

## Stretch goals (if you finish early)

- Add search across your notes
- Add a "pin note" feature that keeps pinned notes on top
- Ask Claude: "where exactly do my notes live on disk?" and go look at the file

## If you get stuck

Paste the exact error back to Claude. The classic here is a **port conflict** ("address
already in use") — tell Claude and it'll pick another port or stop the old process.

**Delete button does nothing — no error, no message?** Claude probably guarded it with a
pop-up "are you sure?" dialog, and those do not appear in the built-in browser, so the
click goes nowhere. This is the one failure here with nothing to paste back. Tell Claude:
*the delete button does nothing — remove the pop-up confirm and use an inline confirm step
on the page instead.*

**Stuck for 10 minutes? Grab a facilitator.**

## Could you ship this? (Part 5 preview)

Not by yourself — and that's the lesson of this track. It needs a running process and a
database, so there's no static hosting path. Sharing it with your team means servers,
backups, and accounts: a handoff conversation with engineering, not a build-and-deploy.
For notes on your own machine, though? Ship it to yourself. It's already shipped.
