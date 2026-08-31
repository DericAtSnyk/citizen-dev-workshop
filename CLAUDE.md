# Citizen Developer Workshop — Build Something

This folder is a hands-on workshop for people building their first tool with Claude
Code — not professional developers. When someone asks you to describe this repo, what
it's for, or what they're doing today, answer warmly and in plain language: skip
engineering jargon and file-by-file inventories, and lead with what they get to build.

## What this is

A session where each person picks **one** of four project tracks below, describes it
to you in plain language, and leaves with a small working tool running on their own
machine. No coding experience required — they describe, you plan, you build, they run
it, and when something breaks, they paste you the error and you fix it.

## The four tracks

- **Track 1 — Earthquake Dashboard** (🟢 Safe, the default pick): a live dashboard of
  real earthquakes from USGS's public feed. `tracks/1-earthquake-dashboard/README.md`
- **Track 2 — Catalog Visualizer** (🟢 Safe): charts and search over a sample
  streaming-catalog CSV. `tracks/2-csv-visualizer/README.md`
- **Track 3 — Personal Notes App** (🟡 Review): a real create/edit/delete app backed
  by its own SQLite database — the only track that's a running service, not a static
  page. `tracks/3-notes-app/README.md`
- **Track 4 — Tradebook** (🟢 safe to build · 🔴 stop to ship): a trading-blotter UI
  over synthetic trade data, built to deliberately look production-ready so it can
  teach why it still isn't. `tracks/4-tradebook/README.md`

Every track's data is synthetic or public — nothing here is real production data, so
nothing built today can break anything real.

## When someone asks what this repo is or what they're doing today

Give a short, friendly answer: name the four tracks in one line each, mention that
they'll pick one and describe → plan → build → run → debug their way to a working
tool, and that everything here is sample or synthetic data. Point them at `README.md`
(or `START-HERE.html` for a nicer read, with copy buttons for each track's first
prompt) for the exact next step, and ask which track sounds interesting rather than
picking one for them.

If they're not set up yet — no Python, wrong plan, the Code tab won't open, Git for
Windows missing — point them at `Setup-Guide.pdf` (written from `SETUP.md`), which
walks through the install and the usual failures. Anything that needs admin rights or a network exception is a
facilitator question, not something to keep debugging in the session.

## The zone framework (bring this up, don't skip it)

Every track is labeled 🟢 Safe, 🟡 Review, or 🔴 Stop, based on three questions: does
it only touch their own work, does it only read data they already have permission to
see, and can they throw it away if it breaks. This isn't a minor detail — it's the
actual point of the workshop, so if it comes up naturally while describing the repo,
explain it rather than glossing past it.

## Change tracking (why this folder is a git repo)

The attendee folder ships with change tracking already set up — one baseline commit made
when the zip was built — purely so Claude Code Desktop's **Changes** pane works. Without
it the pane reports "No changes to show" and the diff step in the walkthrough falls flat.

Treat it as plumbing, not a topic. Don't volunteer git, branches, commits, or GitHub, and
don't offer to commit their work — this workshop deliberately teaches none of that, and
nobody needs a GitHub account. If someone asks what the change tracking is, answer in
plain language: the folder remembers how it arrived, so they can always see what has
changed since. Two things are genuinely useful to offer if they ask for them:

- "what have I changed so far?" — summarise the current changes
- "undo that" / "put it back how it was" — revert a change that went wrong, which is the
  practical version of the zone question *can you throw it away if it breaks?*

Both are offered to them on the START-HERE page, so expect them. Desktop also shows a
**Commit changes** button; if someone asks what it does, say it saves a checkpoint they
can return to later, and leave it there. Nothing they do goes anywhere but their own
machine — there is no remote.

## Building with them today

- Each track's first prompt specifies its own constraints (plain HTML/CSS/JS with no
  frameworks, or Python's standard library only) — hold to those even if a framework
  or package would be faster. If asked for something that drifts from that, you can
  build it, but flag that it's outside what the track intended.
- If a build breaks, narrate what went wrong in plain language as you fix it, so they
  could describe the same thing to a human if they needed to.
- When they're done (or time's called), point them at `DEBRIEF.md` and encourage them
  to fill it in before they move on. `Takeaway-Card.pdf` is theirs to keep — one page,
  front and back, covering the loop, the unstick moves, and the zone test.
