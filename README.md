# Build Something — Citizen Developer Workshop

> **Prefer a friendlier read? Double-click `START-HERE.html`** — same guide, nicer
> format, with copy-paste buttons for each track's first prompt. This file covers the
> identical content in plain text.
>
> **Not set up yet? Open [`Setup-Guide.pdf`](Setup-Guide.pdf)** — the same guide that was
> sent before the session: installing Claude Code Desktop, signing in, and checking Python,
> with the usual failures and their fixes.

**Start here.** Today you'll pick one project track, describe it to Claude, and get a
working tool running on your own machine.

You don't need to write any code. You need to describe what you want, read what Claude
does, and tell it when something looks wrong.

---

## What you need before you start

You should already have these from the setup guide sent before the session. If any are
missing, tell a facilitator **now**, not 15 minutes in — or work through
[`Setup-Guide.pdf`](Setup-Guide.pdf) in this folder, which covers installing and checking
each one.

| Requirement | How to check |
|---|---|
| **Claude Code Desktop** installed, signed in, on a **Pro, Max, Team, or Enterprise** plan | The app opens, shows your account, and the **Code** tab doesn't ask you to upgrade |
| **Python 3** | Ask Claude: `do I have Python installed?` |
| **Windows only:** Git for Windows installed | Ask Claude: `do I have git installed?` |
| **This folder** unzipped and already opened once in Claude Code | You did this in setup — e.g. on your Desktop, not inside the zip file |

That's the whole list. Beyond it, you do **not** need a GitHub account, Node, npm, or
any new admin approvals — every track here works with what's above.

## The guided walkthrough

We do this together at the start of the session, led from the front — nobody has to get
ahead. Steps 1 and 2 you already did during setup, so they take seconds the second time.

1. Open **Claude Code Desktop** and click the **Code** tab at the top center — not *Chat*,
   not *Cowork*. Code is the tab with direct access to your files.
   > **Windows users:** the Code tab needs [Git for Windows](https://git-scm.com/downloads/win)
   > installed the first time you open it — install it and restart the app if prompted.
2. Choose **Local**, click **Select folder**, and pick the `citizen-dev-workshop` folder
   you unzipped before the session. Approve the permission prompt if it appears — that
   folder is the only place Claude will work.
3. **Take the tour.** Which **model** and **effort** you're on, the **permission modes** in
   the dropdown next to the send button, and **Plan Mode**, which makes Claude propose a
   plan before it changes anything. Watch for now — you'll use all three today.
4. **Your first prompt.** Type `list the files in this folder` and press enter. The four
   track folders should come back.
5. **Open this guide.** In Claude's reply, click `START-HERE.html`. It opens in the
   built-in **Browser** pane beside the chat. Everything for the rest of the day is there,
   including a tab per track. Leave it open — the pane has tabs, and what you build later
   opens in its own.
6. **Look at the file view** — the same folder as a file tree. Claude isn't doing anything
   magic; it's reading and writing these files, and you can watch it happen.
7. **Try the built-in terminal.** Type `ls`. It lists the same files Claude just listed — a
   third window onto one folder.
8. **Make the panes yours.** Drag the dividers until chat, browser, files, and terminal sit
   where you want them.
9. **Make your first change.** Type `Add my name to the top of DEBRIEF.md`. Small on
   purpose — the point is watching Claude edit a real file on your machine.
10. **Read the diff.** In Claude's reply the edit shows as `+1 -1` — click it and the diff
    opens right there. This is the habit that matters most today: **Claude proposes, you
    read, you decide.** Then open the **Changes** pane for the wider view: everything
    altered since you unzipped the folder. If that pane says "No changes to show" while
    the chat diff is right there, it has lost track — close and reopen it. The chat is the
    one that's always right.
11. **Meet the tracks** back on the START-HERE page — four projects, each in its own tab.
12. **Pick your track and start.** Copy its first prompt and go. Facilitators are
    circulating.

> **Checkpoint.** You're in the right place when the track folders came back from step 4,
> START-HERE is open in the Browser pane, and your name is in `DEBRIEF.md`. Got there
> early? Hold — we move on as a group. Not there yet? Raise a hand now, while it's still a
> two-minute fix.

## How to work with Claude (the whole method)

**Describe → plan → build → run → debug.** That loop is the entire skill.

- **Describe** what you want in plain language. Your track's README gives you a
  first prompt to copy — start there, then make it yours.
- **Plan first.** For the build itself, ask Claude to *make a plan before writing code*
  (or use Plan Mode). You approve the plan, then it builds.
- **Run it.** Ask Claude to run the tool. It opens in the Browser pane as a **new tab**,
  so START-HERE stays put in the first one — flip between instructions and your project.
  **Check the address bar starts with `http://localhost`.** If it starts with `file://`,
  anything the page loads from a file (a CSV, say) will fail — ask Claude to *serve this
  folder over http and give me the localhost address*.
- **When something breaks — and it will — don't start over.** Copy the error, paste it
  back to Claude, and say "this happened." Claude diagnoses and fixes. That's debugging.
- **If something looks wrong visually**, take a screenshot and share it with Claude.

> **Stuck for more than 10 minutes?** Don't keep troubleshooting alone — grab a
> facilitator. That's what we're here for.

## Pick a track

Every project in this workshop sits in one of three zones. Ask yourself three questions:
*Does it only affect my own work? Does it only read data I already have permission to
see? Can I throw it away if it breaks?* Three yeses = 🟢 Safe. Anything shared, scheduled,
or relied on by others needs 🟡 Review. If it starts looking like a production system,
🔴 Stop and talk to engineering.

| Track | What you build | Zone | Good if you… |
|---|---|---|---|
| [**1 — Earthquake Dashboard**](tracks/1-earthquake-dashboard/) | A live dashboard of real earthquakes, from a public data feed | 🟢 Safe | want the smoothest start (**default track**) |
| [**2 — Catalog Visualizer**](tracks/2-csv-visualizer/) | Charts and search over a spreadsheet of streaming titles | 🟢 Safe | work with spreadsheets/CSVs all day |
| [**3 — Personal Notes App**](tracks/3-notes-app/) | A real running notes app with its own local database | 🟡 Review | want to see how "real" apps work |
| [**4 — Tradebook**](tracks/4-tradebook/) | A trading-desk-style blotter over sample trade data | 🟢 build · 🔴 ship | want to see where the limits are |

Can't decide? Take **Track 1**.

## When you're done (or time is called)

Fill in [`DEBRIEF.md`](DEBRIEF.md) — four questions, two minutes. A few volunteers will
demo what they built. Everything here is sample or synthetic data, so nothing you build
today can break anything real — that's by design.

**Take [`Takeaway-Card.pdf`](Takeaway-Card.pdf) with you.** One page, front and back: the
loop and the four moves that unstick almost everything on one side, how to check work you
did not write on the other. It's the part that's still useful next month.
