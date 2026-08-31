# Setup Guide

## Citizen Developer Workshop — Build Something

**Do Part 1 before you arrive. It takes about fifteen minutes.**

Part 1 is the slow half — installing, signing in, and anything that needs your IT team.
None of it needs the workshop files, so you can do it right now. Part 2 is what we do
together at the start of the session; it is here so you know what is coming, not so you
can do it early.

---

# Part 1 — Before you arrive

## What you need

**A laptop you can install software on.** Yours or company-issued. Windows 10 or 11, or
macOS 12 or later.

**Admin or install rights.** You will install one application, and possibly Python. If
your laptop is locked down, raise it with IT today — this is the one problem that cannot
be fixed in the room.

**A Claude account on a paid plan.** Pro, Max, Team, or Enterprise. The Code tab does not
open on the free plan.

**Network access.** Your work network or VPN needs to reach `claude.ai` and
`api.anthropic.com`, plus `python.org` or your system package manager for the Python step.

## Steps

1. **Download and install Claude Code Desktop.** Use the link sent with this guide, or
   `claude.ai/download`. Install it like any other application — on a Mac, drag it into
   Applications; on Windows, run the installer and follow the prompts.

2. **Open it and sign in.** Use the Claude account you were told to use for this session.
   Once you are in, your account shows in the top corner.

3. **Click the Code tab** at the top center — not Chat, not Cowork. If it prompts you to
   upgrade, you are on a free plan or the wrong account. Sort that out now, not on the
   day. Asking Claude which plan you are on will not work; it cannot see your billing.
   The plan name lives at claude.ai, under Settings then Billing.

4. **Windows only: install Git for Windows.** The Code tab will not open without it. Get
   it from `git-scm.com/downloads/win`, install it, and restart Claude Code Desktop. Most
   Macs already have Git, so Mac users can skip this.

5. **Download and unzip the workshop folder.** Get `citizen-dev-workshop.zip` from the
   same place you got this guide, and unzip it somewhere you will find again in five
   seconds — your Desktop is ideal. You should end up with a folder called
   `citizen-dev-workshop`. Working inside the zip file itself does not work.

6. **Point Claude Code at that folder, and check Python.** In the Code tab, choose
   `Local` as the environment, click Select folder, and pick the `citizen-dev-workshop`
   folder you just unzipped. Approve the permission prompt — that is normal, and that
   folder is the only place Claude will work. Then send Claude this message:

   ```
   do I have Python installed?
   ```

   If Python is missing, ask Claude to install it for you. This is the step most likely
   to need your admin password and a few minutes, which is exactly why it belongs here
   and not in the session.

   Doing this now means the connection is already proven before you walk in. We repeat it
   together at the start of the session, and it takes ten seconds the second time.

## Confirm it worked

Before you close your laptop, check all six:

- [ ] Claude Code Desktop opens without an error
- [ ] You are signed in, and your account shows in the app
- [ ] The Code tab opens without asking you to upgrade
- [ ] The `citizen-dev-workshop` folder is unzipped somewhere you can find in five seconds
- [ ] You opened that folder in Claude Code and approved the permission prompt
- [ ] Claude confirmed Python is installed, or installed it when you asked

**All six? You are ready.** Nothing else to do until the session.

---

# Part 2 — In the session, together

Nothing to do here now. This is a preview so the steps look familiar when we get to them.
We do all of it as a group, led from the front, right after the opening slides.

1. **Open Claude Code Desktop and click the Code tab**, then choose `Local` and select
   your unzipped `citizen-dev-workshop` folder — the same one from Part 1.

2. **Tour the interface together.** Model and effort, permission modes, and Plan Mode.

3. **Send the first prompt** — `list the files in this folder` — and open the session
   guide by clicking `START-HERE.html` in Claude's reply. It opens in the built-in
   Browser pane, right beside the chat, and stays in its own tab all session.

4. **See the same folder three ways.** The file view, the built-in terminal (`ls` lists
   the same files), and the chat. Then rearrange the panes to suit your screen.

5. **Make a small change and read the diff.** A one-line edit to `DEBRIEF.md`, then the
   diff in Claude's reply showing exactly what moved. This is the habit that matters most
   today: Claude proposes, you read, you decide.

6. **Pick a track and start building.** Four projects, described on the START-HERE page,
   each with a first prompt to copy. Undecided? Take Track 1.

From there you work at your own pace, with facilitators circulating. You will not write
any code — you describe what you want, read what Claude does, and tell it when something
looks wrong.

---

# If something goes wrong

**"This app is from an unidentified developer" (Mac).** Right-click the app and choose
Open, instead of double-clicking. If that option is missing, your Mac is probably
centrally managed — ask IT.

**"Windows protected your PC" (SmartScreen).** Click More info, then Run anyway. If that
button is not there, it is a policy block rather than a mistake — ask IT.

**The Code tab asks you to upgrade.** You are on a free plan, or signed into a personal
account instead of the one for this session. Check the plan at claude.ai under Settings
then Billing — Claude itself cannot tell you, since billing is not visible to it.

**The Code tab will not open on Windows.** Almost always missing Git for Windows. Install
it from `git-scm.com/downloads/win`, then restart the app.

**Install or sign-in hangs, or times out.** Usually a network or proxy block. Ask IT to
confirm your network allows `claude.ai` and `api.anthropic.com`, on VPN and off.

**Python will not install, or Claude cannot find it afterwards.** Usually an admin prompt
you missed, or a network block on `python.org` or your package manager. Ask Claude to
show you the exact error, then bring that error to IT.

**"I am not allowed to install anything on this laptop."** Raise it today with IT and your
Forgd contact. This one genuinely cannot wait until the session.

---

# Where to ask for help

**Stuck for more than ten minutes? Stop and ask.** Message your facilitator or your Forgd
contact before the session, so it is fixed by the time we start rather than during it.

Setup is the one part of this workshop you cannot solve by describing it to Claude —
Claude is not running yet. Everything after setup, you can.
