# Excel Reading Patterns

Career path Excel files come in a few layouts. Here's how to handle each.

## Layout 1 — Row-per-level columns (most common)

Level codes in a header row, content in cells below.

```
         | IC2              | IC3              | IC4
---------+------------------+------------------+--------
Strat.   | Executes tasks...| Owns workstream..| Leads...
Writing  | First drafts...  | Polished drafts..| ...
```

```python
import openpyxl

wb = openpyxl.load_workbook('file.xlsx')
ws = wb['Sheet Name']

# Print first 20 rows to understand layout
for i, row in enumerate(ws.iter_rows(min_row=1, max_row=20, values_only=True), 1):
    print(i, row)

# Find the header row (the one containing IC2, IC3 etc.)
LEVEL_CODES = ['IC2','IC3','IC4','IC5','IC6']
header_row = None
for r in ws.iter_rows():
    if any(str(cell.value or '').strip() in LEVEL_CODES for cell in r):
        header_row = r
        break

# Map level → column index
level_col = {}
for cell in header_row:
    val = str(cell.value or '').strip()
    if val in LEVEL_CODES:
        level_col[val] = cell.column

# Extract a row of content by label
def get_row_by_label(label_fragment):
    for row in ws.iter_rows():
        first = str(row[0].value or '').strip()
        if label_fragment.lower() in first.lower():
            return {lc: str(row[level_col[lc]-1].value or '').strip()
                    for lc in level_col}
    return {}
```

## Layout 2 — Tactical/Adaptive split rows

Some sheets have two sub-rows per responsibility category:
```
Category        | IC2 tactical... | IC3 tactical... | ...
  Tactical      | bullet 1        | bullet 1        | ...
  Adaptive      | bullet A        | bullet A        | ...
```

```python
# Look for merged cells or indented rows
# Cells with no value in column A but content in level columns = sub-row
current_category = None
responsibilities = []

for row in ws.iter_rows(min_row=data_start_row, values_only=False):
    col_a = str(row[0].value or '').strip()
    if col_a:
        current_category = col_a
        current_data = {ic: {'tactical':[], 'adaptive':[], 'ownership':'', 'impact':''} 
                        for ic in LEVEL_CODES}
        responsibilities.append({'category': col_a, 'data': current_data})
    else:
        # Sub-row — check if it's tactical or adaptive
        row_label = str(row[1].value or '').strip().lower()
        for lc in LEVEL_CODES:
            val = str(row[level_col[lc]-1].value or '').strip()
            if val and current_data:
                bullets = [b.strip() for b in val.split('\n') if b.strip()]
                if 'tactical' in row_label:
                    current_data[lc]['tactical'].extend(bullets)
                elif 'adaptive' in row_label:
                    current_data[lc]['adaptive'].extend(bullets)
```

## Layout 3 — Skills matrix grid

```
                | Foundational | Intermediate | Advanced | Expert | Strategic
                | (IC2)        | (IC3)        | (IC4)    | (IC5)  | (IC6)
----------------+--------------+--------------+----------+--------+----------
Technical Depth | [signal]     | [signal]     | ...
Writing Quality | [signal]     | ...
```

```python
# Find the skills section — often starts after a labelled header row
skills = []
in_skills_section = False

for row in ws.iter_rows(values_only=True):
    if row[0] and 'skills' in str(row[0]).lower():
        in_skills_section = True
        continue
    if not in_skills_section:
        continue
    
    skill_name = str(row[0] or '').strip()
    if not skill_name:
        continue
    
    skill_data = {}
    for i, lc in enumerate(['IC2','IC3','IC4','IC5','IC6'], 1):
        cell_val = str(row[i] or '').strip()
        if cell_val:
            # split on newlines if bullets are embedded
            lines = [l.strip() for l in cell_val.split('\n') if l.strip()]
            signal = lines[0] if lines else ''
            bullets = lines[1:] if len(lines) > 1 else [cell_val]
            skill_data[int(lc[2:])] = {'signal': signal, 'bullets': bullets}
    
    if skill_data:
        skills.append({'name': skill_name, 'data': skill_data})
```

## Common issues

**Merged cells** — openpyxl returns `None` for non-anchor cells of a merge. If a category
name spans rows, only the first row will have the value:

```python
# Unmerge by propagating values downward
prev_val = None
for row in ws.iter_rows():
    val = row[0].value
    if val is not None:
        prev_val = val
    elif prev_val is not None:
        row[0].value = prev_val  # NOTE: this only works on unmerged sheets
```

Better approach: use `ws.merged_cells` to understand the structure first:
```python
print(ws.merged_cells)
```

**Bullet points in cells** — often stored as `\n` separated strings. Split on `\n` and
strip each item:
```python
bullets = [b.strip() for b in cell_value.split('\n') if b.strip()]
```

**Empty cells at IC6** — sometimes the highest level is incomplete. Always default gracefully:
```python
skill_data.get(current_level, skill_data.get(max(skill_data.keys())))
```

**Print the raw sheet first** — before any complex parsing, always print rows 1–30 to
understand what you're working with. Don't assume layout.
