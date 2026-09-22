#!/usr/bin/env python3
"""
build_org_chart.py

Turn a spreadsheet of people/managers into a visual org chart (PNG + PDF)
using Graphviz. Styled as a clean, neutral corporate chart: white cards,
thin grey borders, bold black names, grey titles -- the kind of chart you'd
actually drop into a leadership deck without it fighting for attention.

Usage:
    python3 build_org_chart.py <input.xlsx|input.csv> <output_basename> [--title "Accounting Org Chart"]

Expected columns (case insensitive, order does not matter). The script will
try to auto detect common header variants:

    Name        -> "name", "employee", "employee name", "full name"
    Title       -> "title", "job title", "role", "position"
    Manager     -> "manager", "reports to", "manager name", "supervisor"
    Department  -> "department", "team", "function", "org", "group"  (optional --
                   shown as a small line inside each box, not colour coded)
    Highlight   -> "highlight", "flag", "flagged", "spotlight"       (optional --
                   any truthy value (yes/true/x/1) gives that person a blue
                   border, e.g. to call out a specific hire or leadership role)
    Email       -> "email", "email address"                          (optional, unused in the chart)

Open headcount / vacant roles: if a row's Name is blank, or is one of
"open", "open hc", "vacant", "tbh", "backfill", "unfilled", "open role"
(case insensitive), it's rendered as a dashed placeholder box with the role
title -- handy for headcount review conversations where you want to show
budgeted-but-unfilled roles alongside the live team.

Rows whose Manager value is blank, or does not match anyone else's Name,
are treated as top of the chart (roots). If there is more than one root,
they are all drawn at the top level side by side -- this is common and not
an error (e.g. a Controller and a VP Tax both reporting to a CFO who isn't
in the data).

Output: <output_basename>.png and <output_basename>.pdf
"""

import sys
import csv
import argparse
import unicodedata
from pathlib import Path

try:
    import graphviz
except ImportError:
    sys.exit(
        "The 'graphviz' Python package is required. Install it with:\n"
        "  pip install graphviz --break-system-packages\n"
        "(The Graphviz binary itself, 'dot', must also be installed on the system.)"
    )

# ---------------------------------------------------------------------------
# Column detection
# ---------------------------------------------------------------------------

COLUMN_ALIASES = {
    "name": ["name", "employee", "employee name", "full name", "person"],
    "title": ["title", "job title", "role", "position"],
    "manager": ["manager", "reports to", "reportsto", "manager name", "supervisor", "line manager"],
    "department": ["department", "team", "function", "org", "group", "sub-team", "sub team"],
    "highlight": ["highlight", "flag", "flagged", "spotlight", "highlighted"],
    "email": ["email", "email address", "e-mail"],
}

OPEN_HC_MARKERS = {"open", "open hc", "open role", "vacant", "tbh", "backfill", "unfilled", "open req", "req"}
FALSY_VALUES = {"no", "false", "0", "n", "-", "none"}


def normalize_header(h):
    return str(h).strip().lower().replace("_", " ")


def detect_columns(headers):
    norm = {normalize_header(h): h for h in headers}
    mapping = {}
    for field, aliases in COLUMN_ALIASES.items():
        for alias in aliases:
            if alias in norm:
                mapping[field] = norm[alias]
                break
    return mapping


def read_rows(path):
    path = Path(path)
    if path.suffix.lower() in (".xlsx", ".xlsm"):
        import openpyxl

        wb = openpyxl.load_workbook(path, data_only=True)
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            return []
        headers = [str(h) if h is not None else "" for h in rows[0]]
        data = []
        for r in rows[1:]:
            if all(c is None for c in r):
                continue
            data.append({headers[i]: r[i] for i in range(len(headers)) if i < len(r)})
        return data
    else:
        with open(path, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            return [row for row in reader if any((v or "").strip() for v in row.values())]


def clean(val):
    if val is None:
        return ""
    return unicodedata.normalize("NFKC", str(val)).strip()


def is_truthy(val):
    v = clean(val).lower()
    return bool(v) and v not in FALSY_VALUES


# ---------------------------------------------------------------------------
# Tree building
# ---------------------------------------------------------------------------


def build_people(rows, colmap):
    if "name" not in colmap and "title" not in colmap:
        sys.exit(
            "Could not find a Name or Title column in the spreadsheet. "
            "Expected a header like 'Name', 'Employee', or 'Full Name'."
        )

    people = {}   # unique id -> record
    name_index = {}  # display name -> id, for resolving "Manager" references
    order = []
    seen_names = set()
    open_counter = 0

    for row in rows:
        raw_name = clean(row.get(colmap.get("name", ""), "")) if "name" in colmap else ""
        title = clean(row.get(colmap.get("title", ""), "")) if "title" in colmap else ""
        manager = clean(row.get(colmap.get("manager", ""), "")) if "manager" in colmap else ""
        department = clean(row.get(colmap.get("department", ""), "")) if "department" in colmap else ""
        highlight = is_truthy(row.get(colmap.get("highlight", ""), "")) if "highlight" in colmap else False

        is_open = (not raw_name) or (raw_name.lower() in OPEN_HC_MARKERS)

        if not raw_name and not title:
            continue  # nothing to show for this row at all

        if is_open:
            open_counter += 1
            uid = f"__open_{open_counter}__"
            display_name = "Open HC"
        else:
            if raw_name in seen_names:
                print(f"Warning: duplicate name '{raw_name}' in spreadsheet, keeping first occurrence.", file=sys.stderr)
                continue
            seen_names.add(raw_name)
            uid = raw_name
            display_name = raw_name
            name_index[raw_name] = uid

        people[uid] = {
            "id": uid,
            "name": display_name,
            "title": title,
            "manager": manager,
            "department": department,
            "highlight": highlight,
            "is_open": is_open,
        }
        order.append(uid)

    return people, name_index, order


def resolve_manager_id(person, name_index):
    mgr = person["manager"]
    if not mgr:
        return None
    return name_index.get(mgr)  # None means orphaned reference


def find_roots_and_orphans(people, name_index):
    roots = []
    orphans = []  # (person_id, raw manager string) where manager didn't resolve
    for uid, p in people.items():
        if not p["manager"]:
            roots.append(uid)
            continue
        resolved = resolve_manager_id(p, name_index)
        if resolved is None:
            orphans.append((uid, p["manager"]))
            roots.append(uid)
    return roots, orphans


def detect_cycles(people, name_index):
    """Return list of person ids involved in a manager cycle (A reports to B who reports to A)."""
    cyclic = []
    for uid in people:
        seen = set()
        cur = uid
        while cur and cur in people:
            mgr_id = resolve_manager_id(people[cur], name_index)
            if not mgr_id or mgr_id not in people:
                break
            if mgr_id in seen or mgr_id == uid:
                cyclic.append(uid)
                break
            seen.add(mgr_id)
            cur = mgr_id
    return cyclic


# ---------------------------------------------------------------------------
# Rendering -- neutral corporate theme: white cards, thin grey borders,
# dashed grey cards for open headcount, optional blue border for
# highlighted people. No department colour coding -- department shows up
# as a small text line inside the card instead.
# ---------------------------------------------------------------------------

BG = "#FFFFFF"
CARD_FILL = "#FFFFFF"
CARD_BORDER = "#D7DBE0"
OPEN_FILL = "#F7F9FB"
OPEN_BORDER = "#B7BEC7"
HIGHLIGHT_BORDER = "#2F5FDE"
EDGE_COLOR = "#C7CBD1"
NAME_COLOR = "#14161A"
TITLE_COLOR = "#6B7280"
DEPT_COLOR = "#8A93A3"
OPEN_TEXT_COLOR = "#7B828C"
TITLE_HEADER_COLOR = "#14161A"


def escape(s):
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def node_label(p):
    if p["is_open"]:
        lines = [f'<font color="{OPEN_TEXT_COLOR}"><i><b>Open HC</b></i></font>']
        if p["title"]:
            lines.append(f'<font color="{OPEN_TEXT_COLOR}" point-size="10">{escape(p["title"])}</font>')
        return "<" + "<br/>".join(lines) + ">"

    lines = [f'<font color="{NAME_COLOR}"><b>{escape(p["name"])}</b></font>']
    if p["title"]:
        lines.append(f'<font color="{TITLE_COLOR}" point-size="10">{escape(p["title"])}</font>')
    if p["department"]:
        lines.append(f'<font color="{DEPT_COLOR}" point-size="9">{escape(p["department"])}</font>')
    return "<" + "<br/>".join(lines) + ">"


def build_graph(people, name_index, title, orientation="TB"):
    g = graphviz.Digraph("org_chart", format="png")
    g.attr(
        rankdir=orientation,
        splines="ortho",
        nodesep="0.35",
        ranksep="0.6",
        bgcolor=BG,
        fontname="Helvetica",
    )
    if title:
        g.attr(label=title, labelloc="t", fontsize="20", fontname="Helvetica-Bold", fontcolor=TITLE_HEADER_COLOR)

    g.attr(
        "node",
        shape="box",
        style="rounded,filled",
        fontname="Helvetica",
        fontsize="11",
        margin="0.18,0.12",
        fillcolor=CARD_FILL,
        color=CARD_BORDER,
        penwidth="1.1",
    )
    g.attr("edge", color=EDGE_COLOR, arrowhead="none", penwidth="1.1")

    for uid, p in people.items():
        if p["is_open"]:
            g.node(uid, label=node_label(p), fillcolor=OPEN_FILL, color=OPEN_BORDER, style="rounded,filled,dashed")
        elif p["highlight"]:
            g.node(uid, label=node_label(p), color=HIGHLIGHT_BORDER, penwidth="2.2")
        else:
            g.node(uid, label=node_label(p))

    for uid, p in people.items():
        mgr_id = resolve_manager_id(p, name_index)
        if mgr_id and mgr_id in people:
            g.edge(mgr_id, uid)

    return g


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Build a visual org chart from a spreadsheet.")
    parser.add_argument("input", help="Path to input .xlsx or .csv file")
    parser.add_argument("output", help="Output file basename (no extension) -- will produce .png and .pdf")
    parser.add_argument("--title", default="", help="Chart title")
    parser.add_argument(
        "--orientation",
        default="TB",
        choices=["TB", "LR"],
        help="TB = top to bottom (default), LR = left to right (better for very wide/flat orgs)",
    )
    args = parser.parse_args()

    rows = read_rows(args.input)
    if not rows:
        sys.exit(f"No data rows found in {args.input}.")

    headers = list(rows[0].keys())
    colmap = detect_columns(headers)

    missing = [f for f in ("name", "manager") if f not in colmap]
    if missing:
        print(
            f"Warning: could not confidently detect column(s) {missing}. "
            f"Detected headers: {headers}. Detected mapping: {colmap}",
            file=sys.stderr,
        )

    people, name_index, order = build_people(rows, colmap)
    if not people:
        sys.exit("No valid rows with a name or title were found.")

    roots, orphans = find_roots_and_orphans(people, name_index)
    cyclic = detect_cycles(people, name_index)

    if orphans:
        print("Note: these people report to a manager name not found elsewhere in the sheet "
              "(they've been placed at the top level -- check for typos in manager names):", file=sys.stderr)
        for uid, mgr in orphans:
            print(f"  - {people[uid]['name']} -> manager listed as '{mgr}'", file=sys.stderr)

    if cyclic:
        names = [people[uid]["name"] for uid in cyclic]
        print(f"Warning: possible reporting-line cycle detected involving: {names}. "
              "These may not render correctly.", file=sys.stderr)

    open_count = sum(1 for p in people.values() if p["is_open"])

    g = build_graph(people, name_index, args.title, args.orientation)

    out_base = args.output
    g.format = "png"
    g.render(out_base, cleanup=True)
    g.format = "pdf"
    g.render(out_base, cleanup=True)

    print(f"Wrote {out_base}.png and {out_base}.pdf")
    print(f"{len(people)} boxes, {len(roots)} at the top level"
          + (f", {open_count} open HC" if open_count else "")
          + (f", {len(orphans)} orphaned manager reference(s)" if orphans else ""))


if __name__ == "__main__":
    main()
