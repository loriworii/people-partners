---
name: tactical-adaptive-career-path
description: >
  Build or redesign career path spreadsheets (.xlsx) using the Tactical+Adaptive performance framework
  (based on Neel Doshi's distinction between convergent/tactical and divergent/adaptive performance).
  Use this skill whenever the user wants to: create a new career path or competency framework, apply
  Tactical+Adaptive to an existing career path, add new levels to a career path, redesign IC or Manager
  tracks, build level definitions for any function (Comms, Data, Finance, Engineering, People, etc.),
  or produce a spreadsheet with Ownership / Tactical / Adaptive / Impact responsibility cells and
  Observable Signal skill cells. Trigger on phrases like "career path", "IC track", "manager track",
  "level framework", "competency framework", "job levels", "adaptive tactical", "apply the framework",
  "add levels", or any request to build, update, or redesign how roles are structured at any level.
---

# Tactical + Adaptive Career Path Builder

You are building a professional career path spreadsheet for a people/HR partner. The output must be
a polished, visually consistent .xlsx file that managers and employees can use for performance
conversations, calibration, and career development.

## Before you start

Read the reference files in order:
1. `references/framework.md` — the T+A content writing philosophy and cell-by-cell guidelines
2. `references/formatting.md` — exact visual specs (colours, fonts, column widths, row heights)
3. `scripts/template.py` — the Python boilerplate you MUST use as the foundation for every build

Do this before writing any content or code. The formatting and content patterns were developed through
extensive iteration and must be followed precisely.

## Workflow

### Step 1 — Clarify scope

Before writing a single line of content, confirm:
- **Track type**: IC track, Manager track, or both?
- **Levels**: Which levels (e.g. IC2–IC6, M2–M7)? Level titles (e.g. Associate → Staff → Principal)?
- **Function**: What team/discipline? (This determines the responsibility domains)
- **Source material**: Is there an existing career path, JD, or sample spreadsheet to reference?
- **Behaviours**: Are there existing behaviours to preserve verbatim? (Default: yes, keep them unchanged)
- **Context**: Company name, industry, any specific products/tools/terminology to embed?

If a file is uploaded, inspect it with Python before asking questions — extract levels, domains,
existing content, and formatting so you can confirm rather than ask from scratch.

### Step 2 — Design the structure

Every spreadsheet follows the same structure regardless of function or number of levels:

| Rows | Content |
|------|---------|
| 1 | Level headers (lime green) |
| 2 | Career path description (grey, merged) |
| 3–7 | 5 responsibility domains (pink label + T+A content) |
| 8–12 | 5 behaviour rows (pink label + behaviour text, UNCHANGED) |
| 13 | Skills & Knowledge Matrix header (grey) |
| 14–19 | 6 skills domains (pink label + skills bullets + Observable Signal) |

**Responsibility domains** vary by function. Choose domains that cover the full scope of the role.
For IC tracks: typically a mix of technical execution, strategic output, stakeholder/influence,
and impact domains. For Manager tracks: always include Team Leadership & People Development as
a dedicated domain — it is not optional.

**Skills domains** follow the same principle. Include Observable Signal in every skills cell — a
specific, verifiable behaviour that proves the skill is present, not a generic description.

### Step 3 — Write the content

Read `references/framework.md` carefully before writing. Key principles:

- **Responsibilities**: Use the `fmt()` helper. Every cell = Ownership + Tactical bullets + Adaptive bullets + Impact
- **Skills**: Use the `skl()` helper. Every cell = existing bullets + `Observable signal:` line
- **Behaviours**: Copy verbatim. Never change the wording, even if the language is imperfect
- **Level progression**: The jump between levels must be felt, not just described. Adaptive is where
  the real differentiation lives — use it to show a qualitatively different way of operating, not
  just "does more of the same"
- **Specificity**: Reference real products, tools, outlets, communities relevant to the function and
  company. Generic content is weak content. At Consensys: MetaMask, Linea, Infura, CoinDesk, The Block,
  Farcaster, on-chain data, DeFi, Layer 2s, etc.

### Step 4 — Build the spreadsheet

Use `scripts/template.py` as your foundation — copy its boilerplate and fill in your content.
Do NOT rebuild the openpyxl formatting from scratch. The template encodes the exact colours, fonts,
merges, and dimensions that have been validated.

**Critical dimensions (non-negotiable):**
- Row 1: 60.0 | Row 2: 37.5 | Rows 3–7: 240.0 | Rows 8–12: 114.75 | Row 13: 37.5 | Rows 14–19: 165.0
- Column A: 33.0 | Column B: 45.0 | All content columns: 63.0 each

Save to the outputs folder: `/sessions/[session-id]/mnt/outputs/[Title] - Tactical + Adaptive.xlsx`

Run the recalc validator after saving:
```
python3 /sessions/[session-id]/mnt/.claude/skills/xlsx/scripts/recalc.py "[output path]"
```
It must return `{"status": "success", "total_errors": 0}`. Fix any errors before delivering.

### Step 5 — Deliver

Share the file with a `computer://` link. Keep the summary brief — one line on what was built,
one line on any significant design decisions (e.g. which domains were chosen and why).

## Common patterns by track type

### IC tracks
- Domains typically: [Craft/Execution domain], [Technical/Tooling domain], [Communication/Storytelling],
  [Stakeholder Influence], [Strategic Impact]
- Lower levels (IC2–IC4): Tactical section is the dominant signal — can they execute reliably?
- Upper levels (IC5–IC7): Adaptive section carries more weight — are they redefining the work itself?
- Skills labels: Foundational → Intermediate → Advanced → Expert → Strategic → Visionary

### Manager tracks
- Always include: Team Leadership & People Development as its own domain
- Strategy domain: escalates from "team/workstream" ownership at M2 to "company-level narrative" at M6/M7
- Skills labels: Manager → Senior Manager → Associate Director → Director → Senior Director → VP
- Behaviours: managers use a different tier of behaviours than ICs (more "lead/model/cultivate" language)
- Observable signals: must be verifiable through real management outcomes (promotions, retention,
  team capability, stakeholder citations) — not just behaviours

### Extending existing tracks
If the user provides an existing spreadsheet and wants to add levels or apply the framework:
1. Extract ALL existing content, formatting, column widths, row heights from the source file
2. Preserve existing level titles exactly
3. New levels should feel like a genuine escalation — not just "more senior version of previous level"
  At M6/M7 or IC6/IC7, the scope shifts from function-level to company-level or industry-level
4. Behaviours: copy unchanged from source, even if they reference the "wrong" team (e.g. "marketing"
  in a comms track) — the user has seen them and approved them

## Quality checks before delivering

- [ ] Every responsibility cell has Ownership, Tactical, Adaptive, and Impact
- [ ] No two adjacent levels have Adaptive bullets that feel interchangeable
- [ ] Every skills cell has an Observable Signal that is specific and verifiable
- [ ] Behaviours are unchanged from source (or from standard set if no source)
- [ ] Level titles match source or confirmed brief exactly
- [ ] recalc.py returns zero errors
- [ ] Column widths are set (not default), row heights are set to accommodate content
