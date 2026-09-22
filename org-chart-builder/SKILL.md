---
name: org-chart-builder
description: Build a visual org chart (PNG and PDF) from a spreadsheet of people, titles, and managers. Use this whenever the user has, or can get, a list of employees with a "reports to" or manager relationship and wants it turned into a chart -- for any team, department, or the whole company (Accounting, Finance, Marketing, Engineering, etc). Trigger on phrases like "org chart", "reporting structure", "who reports to who", "team structure diagram", "map out the hierarchy", or when the user uploads an HR export / headcount list and asks to visualise it. Also trigger if the user references wanting to see a team's structure for a leadership conversation, restructure, or headcount review, even if they don't say "org chart" explicitly.
---

# Org chart builder

Turn a flat list of people into a proper visual org chart. The core problem
this solves: HR/HRIS exports are just rows of names and managers -- nobody
can read a hierarchy out of a spreadsheet at a glance, and leaders want the
picture, not the table.

## When to use this

Use whenever the user wants a reporting structure turned into something
visual -- for a specific team (e.g. "the Accounting org chart"), a whole
function, or a full company. This applies even if they only have a rough
list in their head rather than a file -- in that case, help them turn it
into a small table first (see "No spreadsheet yet" below), then chart it.

## Step 1: Get the data into a spreadsheet shape

The script needs a CSV or XLSX with, at minimum, a **Name** column and a
**Manager** (or "Reports To") column. It also picks up **Title** and
**Department** if present -- department shows up as a small text line
inside the box (not colour coded; the chart style is deliberately neutral:
white cards, thin grey borders, black name, grey title).

If the user already has a file (HRIS export, headcount tracker, etc), use
it directly -- the script auto detects common header variations (e.g.
"Employee Name", "Job Title", "Reports To", "Team"), so don't waste time
renaming columns unless detection fails.

Two optional extras, both off unless the data calls for them:
- **Open headcount.** Give a row a blank Name (or a Name like "Open HC",
  "Vacant", "TBH", "Backfill") and it renders as a dashed grey placeholder
  box with just the role title -- useful for headcount review conversations
  where the live team and the open reqs need to be on the same chart.
- **Highlight.** Add a `Highlight` column (or `Flag`) with a truthy value
  (yes/true/x/1) on a row and that person gets a blue border instead of
  grey -- for calling out a specific hire, a leadership role, or whoever
  the conversation is actually about.

**No spreadsheet yet?** If the user just describes the team verbally or
pastes a rough list, build a small CSV yourself from what they tell you
(Name, Title, Manager, Department) before running the script. Ask for
anyone missing a manager only if it's ambiguous who they report to --
otherwise infer it from context (e.g. "these five all report to the
Controller").

A worked example with fictional names/roles ships in `examples/example_people.csv`
-- use it to sanity check the script or show someone what the output looks
like before they hand over real data.

## Step 2: Run the script

```bash
python3 scripts/build_org_chart.py <input.xlsx or .csv> <output_basename> --title "Accounting Org Chart"
```

This produces `<output_basename>.png` and `<output_basename>.pdf`.

Use `--orientation LR` instead of the default `TB` (top to bottom) when the
org is wide and flat (e.g. one manager with 12 direct reports) -- left to
right reads better in that case than a huge horizontal top row.

Read whatever the script prints to stderr before showing the result to the
user. It will flag:
- **Orphaned manager references** -- someone's manager name doesn't match
  any Name in the sheet (usually a typo, or a manager who sits outside the
  team and isn't in the data -- e.g. the team's chart stops at a VP who
  reports to someone not listed). These people get placed at the top level
  so nobody is dropped from the chart, but flag the mismatch to the user
  so they can confirm it's expected rather than a data error.
- **Cycles** -- A reports to B who reports to A. This is a data problem,
  not a chart problem -- flag it, don't try to silently fix it.

## Step 3: Sanity check before sharing

Before presenting the chart, actually look at it (open the PNG) and check:
- Does the headcount in the chart match the number of rows in the source
  file? If not, some rows were likely skipped (missing name, duplicate
  name) -- the script prints a count, compare it.
- Is anyone floating at the top level who shouldn't be? That's the orphan
  warning from Step 2 -- resolve it with the user rather than shipping a
  chart with a stray box.
- Did any "Open HC" rows render where they shouldn't have (e.g. a real
  person whose name happened to be blank in the source data)? Check the
  open HC count the script prints against what the user actually expects.

## Step 4: Deliver

Save the PNG (for quick viewing/embedding in a deck) and PDF (for print or
sharing as a document) to the user's chosen output location. If this is
going straight into a deck or exec conversation, offer to also drop the PNG
into a slide rather than leaving it as a standalone image -- ask if that's
where it's headed.

## Notes on judgement calls

- **Multiple roots are normal, not an error.** If the sheet is a subset of
  the company (e.g. just Accounting), several people will report to a
  manager who isn't in the data (a CFO, say). They'll all render as
  separate top level boxes -- that's correct, not a bug.
- **Don't over-engineer the visual.** Resist adding extra bells (photos,
  icons, org level numbers, colour coding) unless asked -- a clean, neutral
  box-and-line chart is what actually gets used in a leadership
  conversation. Clutter undermines the "one glance" value of an org chart.
- **Large orgs (50+ people):** the chart will get tall. Suggest `LR`
  orientation or splitting into sub-team charts (e.g. one per manager) if
  a single chart becomes unreadable -- don't just render a giant image and
  call it done.
