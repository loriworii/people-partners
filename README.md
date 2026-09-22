# people-partners
# Claude Skills

A collection of Claude skills for People/HR workflows at Consensys — org design, career pathing, and related tooling.

## Skills

### org-chart-builder
Builds a visual org chart (PNG + PDF) from a spreadsheet of names, titles, and managers. Auto detects common HR export column names, supports open headcount placeholders and highlighting specific people.

### tactical-adaptive-career-path
Builds or redesigns career path spreadsheets using the Tactical+Adaptive performance framework — IC and Manager tracks, level definitions, competency cells.

### career-framework-builder
Turns a career path spreadsheet into an interactive HTML tool — level browsing, skill definitions, and a self assessment that generates a development plan.

## How to use

Each skill is a `.skill` file (a zip containing `SKILL.md` and any bundled scripts/references). To use one:

1. Unzip it.
2. Drop the resulting folder into your Claude skills directory, or upload the `.skill` file directly in Cowork/Claude Code, which installs it.

Claude reads `SKILL.md` for instructions and triggers automatically based on its description — no manual invocation needed.
