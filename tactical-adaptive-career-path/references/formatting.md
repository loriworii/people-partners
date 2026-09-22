# Visual Formatting Specification

All career path spreadsheets use these exact values. Do not improvise. These were validated through
multiple iterations and match the established design system.

## Colours

| Role | Hex | Usage |
|------|-----|-------|
| FILL_HEADER | `C1FF14` | Level header row (Row 1), lime green |
| FILL_SECTION | `FF62E6` | Section labels (A3, A8, A14 merged cells), pink |
| FILL_TITLE | `EFEFEF` | Title rows (Row 2, Row 13), light grey |
| FILL_WHITE | `FFFFFF` | All content cells |

## Typography

- Font family: **DM Sans** for all cells
- Header row (Row 1): size 10, bold=True
- Section labels (A3, A8, A14): size 10, bold=True
- Domain labels (B column): size 9, bold=True
- Content cells: size 9, bold=False, wrap_text=True, valign=center
- Title cells: size 9, bold=True, wrap_text=True

## Column widths

| Column | Width | Content |
|--------|-------|---------|
| A | 33.0 | Section labels (merged rows) |
| B | 45.0 | Domain/behaviour names |
| All content columns | 63.0 | Level content cells — all equal width |

Set all content columns (C onward) to **63.0** each. Use openpyxl's column_dimensions loop rather
than trying to set a range — set the same width for each content column letter.

## Row heights

| Row(s) | Height | Content |
|--------|--------|---------|
| Row 1 | 60.0 | Level headers |
| Row 2 | 37.5 | Career path title (merged) |
| Rows 3–7 | 240.0 | Responsibility cells (T+A format) |
| Rows 8–12 | 114.75 | Behaviour rows |
| Row 13 | 37.5 | Skills header |
| Rows 14–19 | 165.0 | Skills cells with Observable Signal |

These are the exact values from the validated reference file. Do not adjust upward — 240 is
sufficient for T+A content when columns are 63.0 wide.

## Merged cells

```
A2:B2            — Career path description, left side
[last_col]2      — Career path description, merged across content columns
A3:A7            — "Responsibilities" section label
A8:A12           — "Behaviours" section label
A13:B13          — Skills & Knowledge Matrix header
A14:A19          — "Skills & Knowledge Matrix" section label
C2:[last_col]2   — Career path description, content columns merged
```

For a 5-level track (C–G): last_col = G
For a 6-level track (C–H): last_col = H
For a 4-level track (C–F): last_col = F

Adjust merge ranges accordingly.

## Cell alignment

- Section labels (A3, A8, A14): h="center", v="center"
- Level headers (Row 1, content cols): h="center", v="center"
- Domain labels (B column): h="left", v="center"
- All content cells: h="left", v="center", wrap_text=True
- Title/header row text: h="center" for content columns, h="left" for A/B

## Python styling pattern

```python
from openpyxl.styles import PatternFill, Font, Alignment

FILL_HEADER  = PatternFill("solid", fgColor="C1FF14")
FILL_SECTION = PatternFill("solid", fgColor="FF62E6")
FILL_TITLE   = PatternFill("solid", fgColor="EFEFEF")
FILL_WHITE   = PatternFill("solid", fgColor="FFFFFF")

def fnt(bold=False, size=9, name="DM Sans"):
    return Font(bold=bold, size=size, name=name)

def aln(h="left", v="center", wrap=True):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)

def style(cell, fill, font, alignment):
    cell.fill = fill
    cell.font = font
    cell.alignment = alignment
```

## Skills level label progression

IC tracks:
```
Foundational | Intermediate | Advanced | Expert | Strategic | Visionary
```

Manager tracks:
```
Manager | Senior Manager | Associate Director | Director | Senior Director | VP
```

For tracks with fewer levels, use the first N labels from the appropriate progression.

## Validation

After building, always run:
```bash
python3 /sessions/[session]/mnt/.claude/skills/xlsx/scripts/recalc.py "[output_path]"
```

Expected response: `{"status": "success", "total_errors": 0, ...}`

If errors appear, inspect the output — common causes are: mismatched merge ranges, cells written
after merging (write to top-left cell of merge range only), or missing fill on cells adjacent to
merged ranges.
