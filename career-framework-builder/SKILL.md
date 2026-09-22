---
name: career-framework-builder
description: >
  Build an interactive, self-contained HTML career framework tool from an Excel career path file
  or written description. Produces a polished single-file HTML app with level browsing, skill
  definitions, and a 3-step self-assessment that generates a personalised development plan with
  a 1:1 conversation guide. Supports IC track, Manager track, or dual-track with a switcher.
  Use this skill whenever someone asks to build a career framework tool, interactive career path,
  self-assessment tool for career levels, development plan generator, or wants to turn a career
  path spreadsheet into something employees can actually use. Also trigger if the user mentions
  phrases like "career framework", "career path interactive", "IC track tool", "level framework
  HTML", "make this career path usable", or "build a self-assessment" in a people/HR context.
---

# Career Framework Builder

You are building a **self-contained single-file HTML interactive tool** that lets employees
browse their career framework and run a self-assessment to generate a personalised development
plan. Everything lives in one `.html` file — no server, no dependencies except a Google Fonts
CDN call.

The tools you've built before (Data Analytics, External Comms, Product & Biz Ops) all follow
this pattern and are the gold standard. Build to that quality bar.

---

## Step 1 — Gather what you need

Before writing any code, establish:

1. **Data source** — has the user uploaded an Excel file? If yes, read it with openpyxl. If not,
   ask for a description of the levels, responsibilities, and skills.

2. **Track scope** — IC only, Manager only, or dual-track (IC + Manager with a switcher)?
   Default to IC-only unless told otherwise. For dual-track, ask about the manager level range
   (e.g. M2–M7).

3. **Function/team name** — this goes in the header and as the 2-letter brand dot (e.g. "DA"
   for Data Analytics, "EC" for External Comms, "BO" for Business Ops).

4. **Output path** — where to save the file. Default to the user's workspace folder.

---

## Step 2 — Extract data from Excel

Use openpyxl, not pandas, so you can read merged cells and formatting correctly.

```python
import openpyxl
wb = openpyxl.load_workbook('/path/to/file.xlsx')
```

Look for these structures (they vary by sheet layout — be adaptive):

- **Level headers** — usually in a header row, columns for each level (IC2–IC6, M2–M7, etc.)
- **Responsibility rows** — often grouped by category with subcategories
- **Behaviour rows** — typically 4–6 rows with values per level
- **Skills matrix** — a grid where rows are skill areas and columns are levels

If the sheet uses a tactical/adaptive split (two sub-rows per responsibility category), capture
both. If it's a flat list per level, treat as tactical only.

Print the sheet structure first to understand the layout before extracting:

```python
for row in ws.iter_rows(min_row=1, max_row=25, values_only=True):
    print(row)
```

---

## Step 3 — Build the HTML via a Python script

**Critical pattern:** Write the full HTML as a Python script that outputs the file, rather than
writing HTML directly. This is important because:

- JavaScript string literals need apostrophes escaped as `\'`. Python's raw strings make this
  natural — you write the JS escape directly without Python also needing to escape it.
- You can run `node --check` on the extracted JS to catch syntax errors before declaring done.
- It's easy to iterate: run the script again, get a fresh validated output.

Structure your build script as:

```python
#!/usr/bin/env python3
# Build script: generates the career framework HTML

# 1. Define all data as Python dicts/lists
# 2. Build the HTML string (CSS + HTML + JS with data inline)
# 3. Write to output file
# 4. Run node --check to validate JS syntax
# 5. Print result
```

---

## Step 4 — The HTML structure

The output file should follow this layout:

### Head
```html
<title>[Function] Career Framework | Consensys</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
```

### CSS — always use these variables
```css
:root {
  --navy: #1A1A2E; --navy-mid: #16213E; --navy-light: #0F3460;
  --orange: #F6851B; --orange-light: #F9A65A;
  --orange-pale: rgba(246,133,27,0.12); --orange-pale2: rgba(246,133,27,0.06);
  --white: #FFFFFF; --offwhite: #F7F8FA;
  --grey-800: #2D3340; --grey-600: #5A6270; --grey-400: #9AA3AD;
  --green: #1DB87C; --amber: #F59E0B; --red: #EF4444; --blue: #3B82F6;
}
body { font-family: 'DM Sans', sans-serif; background: var(--offwhite); color: var(--grey-800); }
```

### Header
```html
<header class="site-header">
  <div class="header-brand">
    <div class="brand-dot">[2-LETTER ABBREV]</div>
    <span class="brand-text">[Function] <span>Career Framework</span></span>
  </div>
  <nav class="header-nav">
    <button class="nav-btn active" onclick="setView('browse')">Browse</button>
    <button class="nav-btn" onclick="setView('assess')">Self-assessment</button>
  </nav>
</header>
```

### Level pills
Level selector bar — clicking sets `currentLevel` and calls `render()`. Active pill gets
orange background.

### Browse view tabs
Three tabs: Responsibilities | Behaviours | Skills
Each renders the content for `currentLevel`.

### Assessment view — 3 steps
Step 1: Rate each skill on a 4-point scale (Not there yet / Getting there / Nailing it / Beyond this level). Each skill card has a notes textarea.

Step 2: Career goals form — short term, mid term, long term text inputs + career direction dropdown.

Step 3: Development plan — generated from ratings. Shows strengths, priority gaps with goal cards, 1:1 conversation guide, copy-to-clipboard button.

---

## Step 5 — JavaScript data structures

These are the exact structures the assessment logic expects. Stick to them precisely.

### Levels
```javascript
const icLevels = {
  2: {code:'IC2', title:'[title]', badge:'[badge label]', badgeClass:'b-foundational'},
  3: {code:'IC3', title:'[title]', badge:'[badge]', badgeClass:'b-intermediate'},
  // ... up to IC6
};
// Badge classes: b-foundational, b-intermediate, b-advanced, b-expert, b-strategic
```

### Responsibilities
```javascript
const icResponsibilities = [
  {category:'[Category Name]', data:{
    2:{ownership:'[who owns what at this level]',
       tactical:['bullet','bullet','bullet'],
       adaptive:['bullet','bullet'],
       impact:'[what good looks like from the outside]'},
    // ... repeat for 3,4,5,6
  }},
  // ... more categories
];
```

### Behaviours
```javascript
const icBehaviours = [
  {name:'[Value Name]', data:{
    2:'[expectation at IC2-IC4 level]',
    5:'[elevated expectation at IC5-IC6 level]'
    // behaviours typically have 2 tiers — junior and senior
  }},
];
```

### Skills (this is what drives the assessment)
```javascript
const icSkills = [
  {name:'[Skill Area Name]', data:{
    2:{signal:'[observable signal — what "nailing it" looks like at IC2]',
       bullets:['specific thing','specific thing','specific thing']},
    3:{signal:'[...]', bullets:[...]},
    // ... up to IC6
  }},
];
```

### Lead support asks (one per skill, per rating level)
```javascript
const icLeadSupport = {
  '[Skill Area Name]':{
    1:'[what to ask lead when "not there yet"]',
    2:'[what to ask when "getting there"]',
    3:'[what to ask when "nailing it" — push to next level]'
  },
  // ... one entry per skill
};
```

### Timeframes — CRITICAL: must be wired into the active variable system
```javascript
const icTimeframes = {1:'60 days', 2:'next quarter', 3:'3–6 months'};
const mgrTimeframes = {1:'90 days', 2:'next quarter', 3:'3–6 months'}; // if manager track
```

### Active track variables — declare ALL of them here
```javascript
let levels = icLevels, responsibilities = icResponsibilities, behaviours = icBehaviours;
let skills = icSkills, leadSupport = icLeadSupport, careerOptions = icCareerOptions;
let timeframes = icTimeframes;  // ← DO NOT omit this. It causes a silent runtime crash.
```

### Career options
```javascript
const icCareerOptions = [
  {value:'', label:'Select where you\'re heading...'},
  {value:'specialist', label:'[option label]'},
  // ... 7-9 options relevant to the function
];
```

### setTrack() — swap ALL variables including timeframes
```javascript
function setTrack(track) {
  currentTrack = track;
  // reset state...
  if (track === 'manager') {
    levels = mgrLevels; responsibilities = mgrResponsibilities; behaviours = mgrBehaviours;
    skills = mgrSkills; leadSupport = mgrLeadSupport; careerOptions = mgrCareerOptions;
    timeframes = mgrTimeframes;  // ← must be here too
  } else {
    levels = icLevels; responsibilities = icResponsibilities; behaviours = icBehaviours;
    skills = icSkills; leadSupport = icLeadSupport; careerOptions = icCareerOptions;
    timeframes = icTimeframes;  // ← and here
  }
  // ...
}
```

---

## Step 6 — Assessment logic

### renderGoalCard(skill, priority)
Uses `timeframes[r]` where r is the rating (1–4). This crashes if `timeframes` isn't declared
as an active variable — see Step 5.

```javascript
function renderGoalCard(skill, priority) {
  const d = skill.data[currentLevel];
  const nextD = currentLevel < maxLvl ? skill.data[currentLevel+1] : null;
  const tf = timeframes[r] || 'next quarter';
  const ls = leadSupport[skill.name]
    ? (leadSupport[skill.name][r] || leadSupport[skill.name][2])
    : 'Ask your lead for a specific project or opportunity to develop this skill.';
  // ...build goal card HTML
}
```

### render1on1(gaps, developing, beyonds, lev, nextLev)
Generates a structured 1:1 conversation guide — how to open, how to share gaps, how to
articulate career goals, how to ask for support, how to discuss progression if relevant, how
to close with a follow-up date.

### copyPlan()
Copies the full development plan as plain text to clipboard, formatted for pasting into a
1:1 doc or Notion.

### getAlignmentData(direction, level)
Returns a card with `type`, `icon`, `title`, `body`, `tips[]` based on the selected career
direction. Dispatches to `icGetAlignmentData` or `mgrGetAlignmentData` based on `currentTrack`.
Write 8–10 direction options per track, with honest framing about alignment (strong/partial),
not generic positivity.

---

## Step 7 — Apostrophe safety

JavaScript strings in this file will contain lots of prose text — contractions, possessives,
names. Every apostrophe inside a single-quoted JS string literal must be escaped as `\'`.

When writing data in Python, escape at the source:
- `"don\'t"` → writes `don\'t` into the JS
- `"the team\'s approach"` → writes `the team\'s approach` into the JS

If fixing an existing file (not building fresh), use these two regex patterns to catch
unescaped apostrophes safely:

```python
import re

def fix_apostrophes(text):
    # Pattern 1: contractions (letter + ' + letter)
    text = re.sub(r"(?<!\\)([a-zA-Z\d])'([a-zA-Z])", r"\1\\'\2", text)
    # Pattern 2: possessives (letter + ' + space + letter)
    text = re.sub(r"(?<!\\)([a-zA-Z])'(?=\s[a-zA-Z])", r"\1\\'", text)
    return text
```

Do NOT use a broader pattern that includes `,` or `)` in the second group — it will incorrectly
escape string delimiters like `'browse',`.

---

## Step 8 — Validate before declaring done

Always run this before saving the final output:

```python
import subprocess

with open('/tmp/test_js.js', 'w') as f:
    f.write(js_only)  # JS extracted from between <script> and </script>

result = subprocess.run(['node', '--check', '/tmp/test_js.js'], capture_output=True, text=True)
if result.returncode != 0:
    print("JS SYNTAX ERROR:")
    print(result.stderr[:800])
    # Do NOT save the file until this passes
else:
    print("✅ JS syntax OK")
```

If `node` isn't available, fall back to checking for unescaped apostrophes manually by
searching for `[a-zA-Z]'[a-zA-Z,\s)]` in the JS block.

---

## Step 9 — Content quality bar

The framework data should feel like it was written by a thoughtful senior person in that
function — not generic. Each skill's signal should be a concrete observable behaviour
("Senior journalists proactively reach out to them for comment"), not a vague standard
("demonstrates excellence"). The lead support asks should be specific asks to a manager,
not generic coaching advice.

For career direction alignment cards, be honest about fit. Not every direction is "well
aligned" — say "partially aligned" where true, and explain the gap clearly.

---

## Output

- Save the `.html` file to the user's workspace folder
- Name it: `[FunctionAbbrev]_[Track]_Career_Framework_Interactive.html`
  - Examples: `ExternalComms_IC_Career_Framework_Interactive.html`
  - `DataAnalytics_IC_Career_Framework_Interactive.html`
  - `ProductBizOps_IC_Career_Framework_Interactive.html`
- Link to it with a `computer://` URL
- Do not add a README unless asked

---

## Common mistakes to avoid

1. **Forgetting `timeframes` in the active variables** — causes a silent crash when the
   development plan tries to render. Always declare `let timeframes = icTimeframes;` alongside
   the other active variables, and swap it in `setTrack()`.

2. **Unescaped apostrophes in JS strings** — any text with contractions or possessives copied
   from an Excel cell will break the JS. Always escape at write time in Python.

3. **Using `data_only=True` in openpyxl** — this reads the cached value from the last time
   the file was saved in Excel, not the current formula value. Use default load (no flag).

4. **Modifying HTML directly for complex changes** — write a new Python build script and
   regenerate from scratch. Direct HTML edits on 1000+ line files produce subtle bugs.

5. **Missing `node` syntax check** — the file might look valid but crash at runtime because
   of an apostrophe 300 lines in. Always check.

6. **`behaviours` data shaped as level → string, not level → object** — renderBehaviours
   expects `behaviour.data[level]` to be a string. Keep it that way; don't wrap it in `{text:...}`.

---

## References

See `references/example-data-shape.md` for a complete annotated example of all data
structures for a single-track tool, based on the Data Analytics framework.

See `references/branding.md` for the full CSS variable set and component styles.
