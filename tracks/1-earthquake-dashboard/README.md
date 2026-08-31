# Track 1 — Earthquake Dashboard 🟢 Safe

**Zone: 🟢 Safe** — it only reads a public data feed, affects nothing but your own
machine, and you can delete it without consequence.

## What you'll build

A single-page dashboard showing earthquakes from the last 24 hours, using the U.S.
Geological Survey's public earthquake feed. Live, real data — no account, no API key,
no sign-up. Just a web page that fetches and displays it.

## What it teaches

- Calling a **live public API** and showing the result
- Handling refresh (new data arrives constantly) and errors (what if the feed is down?)
- That a useful tool can be **one single file** with no server behind it

## Your first prompt

Copy this into Claude, then adjust it to taste:

> Build me a single-page earthquake dashboard as one self-contained `index.html` file
> inside `tracks/1-earthquake-dashboard/` — plain HTML, CSS, and JavaScript, no frameworks
> and nothing to install.
> It should fetch the last 24 hours of earthquakes from the USGS public GeoJSON feed at
> `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`, show a
> summary (how many quakes, strongest magnitude), and a sortable table of the biggest
> ones with place, magnitude, and time. Add a refresh button, and show a friendly
> message if the feed can't be reached. Make a short plan first before writing code.
>
> When it is built, start a local web server in this folder with Python and **open** the
> resulting `http://localhost` page in the browser. If a tab is showing this same page
> from a file path, close that one — but leave every other tab open, including the
> workshop guide.

Claude will start a small web server and open the page for you. Check the address bar
says `localhost` — if you are looking at a long file path instead, that is the file
preview, not your running app. See **If you get stuck**.

## Stretch goals (if you finish early)

- Color-code rows by magnitude (green / orange / red)
- Add a filter: "only show magnitude 4.0 and above"
- Auto-refresh every 60 seconds — and ask Claude what changed in the code to do that

## If you get stuck

Paste the exact error (or a screenshot) back to Claude and ask it to fix it. If nothing
appears in the browser, tell Claude what you see — a blank page and an error page are
different clues.

**Two tabs with the same name?** Desktop previews the file it just wrote as well as the
served page. The working one says `localhost` in the address bar, and Claude's message
has an **Open** button that always goes to it. To clear the other, say *close the tab
showing this page as a local file*. You may also see an orange warning that a tab
"shows a single file and can't follow links" — that is the same preview tab, and it goes
away when the tab does.

**Stuck for 10 minutes? Grab a facilitator.**

## Could you ship this? (Part 5 preview)

Yes — this is the textbook shippable case. It's a static page with no server, no
credentials, and only public data. Hosting it is a copy-paste, not an engineering
project.
