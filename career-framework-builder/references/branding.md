# Consensys Career Framework — Branding Reference

## CSS Variables (full set)

```css
:root {
  /* Core palette */
  --navy:         #1A1A2E;
  --navy-mid:     #16213E;
  --navy-light:   #0F3460;
  --orange:       #F6851B;
  --orange-light: #F9A65A;
  --orange-pale:  rgba(246,133,27,0.12);
  --orange-pale2: rgba(246,133,27,0.06);

  /* Neutral */
  --white:    #FFFFFF;
  --offwhite: #F7F8FA;
  --grey-100: #F0F2F5;
  --grey-200: #E2E6EA;
  --grey-400: #9AA3AD;
  --grey-600: #5A6270;
  --grey-800: #2D3340;

  /* Status */
  --green:       #1DB87C;
  --green-pale:  rgba(29,184,124,0.1);
  --blue:        #3B82F6;
  --blue-pale:   rgba(59,130,246,0.1);
  --amber:       #F59E0B;
  --amber-pale:  rgba(245,158,11,0.1);
  --red:         #EF4444;
  --red-pale:    rgba(239,68,68,0.1);
}
```

## Typography

```css
/* Google Fonts import — always include this in <head> */
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">

body {
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 15px;
  line-height: 1.6;
}
```

## Header component

```css
.site-header {
  background: var(--navy);
  padding: 0 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 12px rgba(0,0,0,0.3);
}

.brand-dot {
  width: 32px; height: 32px;
  background: var(--orange);
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 12px;
  color: white; letter-spacing: -0.5px;
}
```

## Nav buttons (view toggle)

```css
.nav-btn {
  padding: 8px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-size: 14px; font-weight: 500;
  background: transparent;
  color: rgba(255,255,255,0.65);
  transition: all 0.18s;
}
.nav-btn.active { background: var(--orange); color: white; font-weight: 600; }
.nav-btn:hover:not(.active) { background: rgba(255,255,255,0.08); color: white; }
```

## Level pills

```css
.level-pill {
  padding: 7px 16px;
  border-radius: 999px;
  border: 2px solid var(--grey-200);
  background: white;
  cursor: pointer;
  font-size: 13px; font-weight: 500;
  color: var(--grey-600);
  transition: all 0.15s;
}
.level-pill:hover { border-color: var(--orange); color: var(--orange); }
.level-pill.active { background: var(--orange); border-color: var(--orange); color: white; font-weight: 600; }
```

## Tab buttons (Responsibilities / Behaviours / Skills)

```css
.tab-btn {
  flex: 1;
  padding: 9px 12px;
  border: none; background: transparent;
  border-radius: 7px;
  font-size: 13px; font-weight: 500;
  color: var(--grey-600);
  cursor: pointer; transition: all 0.15s;
}
.tab-btn.active { background: var(--orange); color: white; font-weight: 600; }
```

## Assessment step indicator

```css
.step { color: var(--grey-400); border-bottom: 2px solid transparent; padding-bottom: 4px; }
.step.active { color: var(--orange); border-bottom-color: var(--orange); }
.step.done { color: var(--green); }
```

## Rating buttons (self-assessment)

4 rating levels:
- 1 = "Not there yet" → red
- 2 = "Getting there" → amber
- 3 = "Nailing it" → green
- 4 = "Beyond this level" → blue/orange

```css
.rating-btn.sel-1 { background: var(--red-pale); border-color: var(--red); color: var(--red); }
.rating-btn.sel-2 { background: var(--amber-pale); border-color: var(--amber); color: var(--amber); }
.rating-btn.sel-3 { background: var(--green-pale); border-color: var(--green); color: var(--green); }
.rating-btn.sel-4 { background: var(--orange-pale); border-color: var(--orange); color: var(--orange); }
```

## Meta chips (results header summary)

```css
.meta-chip { padding: 4px 10px; border-radius: 999px; font-size: 11px; font-weight: 600; }
.mc-red   { background: var(--red-pale);   color: var(--red); }
.mc-amber { background: var(--amber-pale); color: var(--amber); }
.mc-green { background: var(--green-pale); color: var(--green); }
.mc-blue  { background: var(--blue-pale);  color: var(--blue); }
```

## Goal card (development plan)

Three priority levels: high (priority gap), med (developing), low (growth edge):

```css
.goal-card { background: white; border-radius: 12px; padding: 20px; margin-bottom: 14px; border-left: 4px solid; }
.goal-card.priority-high { border-left-color: var(--red); }
.goal-card.priority-med  { border-left-color: var(--amber); }
.goal-card.priority-low  { border-left-color: var(--navy); }

.priority-tag { padding: 2px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
.pt-high { background: var(--red-pale);   color: var(--red); }
.pt-med  { background: var(--amber-pale); color: var(--amber); }
.pt-low  { background: var(--orange-pale); color: var(--orange); }
```

## 1:1 Guide section

```css
.one-on-one {
  background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
  border-radius: 16px;
  padding: 28px 32px;
  margin: 28px 0;
  color: white;
}
.convo-quote {
  background: rgba(255,255,255,0.08);
  border-left: 3px solid var(--orange);
  border-radius: 4px;
  padding: 12px 16px;
  font-style: italic;
  font-size: 13px;
  line-height: 1.7;
  color: rgba(255,255,255,0.9);
}
```

## Results header

```css
.results-header {
  background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
  border-radius: 16px;
  padding: 28px 32px;
  margin-bottom: 24px;
  color: white;
}
```

## Primary action button

```css
.nav-primary {
  background: var(--orange);
  color: white;
  border: none;
  border-radius: 10px;
  padding: 13px 28px;
  font-size: 14px; font-weight: 600;
  cursor: pointer; transition: all 0.18s;
}
.nav-primary:hover { background: var(--orange-light); }
```

## Copy button (plan export)

```css
.copy-btn {
  width: 100%;
  padding: 13px;
  background: transparent;
  color: var(--orange);
  border: 2px solid var(--orange);
  border-radius: 10px;
  font-size: 14px; font-weight: 600;
  cursor: pointer; transition: all 0.18s;
  margin-bottom: 12px;
}
.copy-btn:hover { background: var(--orange-pale); }
.copy-btn.copied { background: var(--green); border-color: var(--green); color: white; }
```

## Hero section (optional, for tools with a landing section)

```css
.hero {
  background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
  border-radius: 16px;
  padding: 36px 40px;
  margin-bottom: 28px;
  color: white;
  position: relative; overflow: hidden;
}
/* Decorative circles */
.hero::before {
  content: '';
  position: absolute; top: -40px; right: -40px;
  width: 200px; height: 200px;
  background: var(--orange); border-radius: 50%; opacity: 0.06;
}
```

## Badge classes (skill level indicators)

```
b-foundational  → IC2 / M2 — indigo tones
b-intermediate  → IC3 / M3 — blue tones
b-advanced      → IC4 / M4 — green tones
b-expert        → IC5 / M5 — amber/gold tones
b-strategic     → IC6 / M6+ — pink/rose tones
```
