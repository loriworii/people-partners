# Example Data Shape — Single IC Track Tool

This is an annotated skeleton showing the complete JS data structure for a single-track
IC tool. Use this as a template and fill in the actual content from the career path data.

---

## Levels object

```javascript
const icLevels = {
  2: {code:'IC2', title:'Associate [Role]',       badge:'Associate',    badgeClass:'b-foundational'},
  3: {code:'IC3', title:'[Role]',                  badge:'Mid-level',    badgeClass:'b-intermediate'},
  4: {code:'IC4', title:'Senior [Role]',           badge:'Senior',       badgeClass:'b-advanced'},
  5: {code:'IC5', title:'Staff [Role]',            badge:'Staff',        badgeClass:'b-expert'},
  6: {code:'IC6', title:'Principal / Head of [F]', badge:'Principal',    badgeClass:'b-strategic'},
};
```

## Responsibilities — tactical/adaptive split

```javascript
const icResponsibilities = [
  {
    category: 'Strategy & Planning',
    data: {
      2: {
        ownership: 'Executes defined tasks within a supervised project plan.',
        tactical: [
          'Completes assigned deliverables on time with quality',
          'Flags blockers early rather than missing deadlines',
          'Follows established processes without needing reminders'
        ],
        adaptive: [
          'Spots one improvement to a process and proposes it',
          'Asks clarifying questions to understand the "why" before starting work'
        ],
        impact: 'Work is delivered reliably without requiring senior oversight for routine tasks.'
      },
      3: {
        ownership: 'Owns a workstream end to end within a defined project.',
        tactical: [
          'Plans and delivers workstream milestones without daily check-ins',
          'Identifies dependencies and manages them proactively'
        ],
        adaptive: [
          'Anticipates scope creep and raises it before it becomes a problem',
          'Proposes improvements to the plan mid-project when the context shifts'
        ],
        impact: 'Projects they own land on time and scope — rarely require senior rescue.'
      },
      // ... IC4, IC5, IC6
    }
  },
  // ... more categories
];
```

**Notes on ownership text:** One sentence describing what the person is accountable for
at this level — scope of authority, not a list of tasks.

**Notes on impact text:** What does "good" look like from the outside? Observable outcome,
not internal activity.

## Behaviours — two tiers (junior and senior)

```javascript
const icBehaviours = [
  {
    name: 'Ownership',
    data: {
      // IC2, IC3, IC4 share this expectation
      2: 'Takes responsibility for their own work, follows through on commitments, and raises blockers promptly rather than letting them fester.',
      // IC5, IC6 share this elevated expectation — key is LEVEL 5 entry
      5: 'Models ownership across the team — proactively fills gaps, makes calls when others hesitate, and creates a culture where accountability is the default, not the exception.'
    }
  },
  {
    name: 'Impact-driven',
    data: {
      2: 'Understands how their work connects to team goals. Focuses on quality output, not just activity.',
      5: 'Consistently ties work to business outcomes. Challenges the team to prioritise by impact, not by volume.'
    }
  },
  {
    name: 'Collaboration',
    data: {
      2: 'Works constructively with teammates, communicates clearly, and supports others when asked.',
      5: 'Actively builds alignment across functions. Creates the conditions for high-quality cross-team work, not just participating in it.'
    }
  },
  {
    name: 'Growth mindset',
    data: {
      2: 'Receives feedback openly and iterates. Proactively seeks learning opportunities relevant to their role.',
      5: 'Creates learning environments for others. Identifies skill gaps in the team and takes action to close them.'
    }
  },
  {
    name: 'Integrity & Trust',
    data: {
      2: 'Is honest about progress, setbacks, and capability. Can be relied on to do what they say.',
      5: 'Maintains trust at scale — with leadership, team, and external stakeholders. Speaks up when something is wrong, even when it\'s uncomfortable.'
    }
  }
];
```

**Notes:**
- Keep 4–6 behaviours max
- Two tiers is standard — IC2-IC4 share one expectation, IC5-IC6 share another
- Render in `renderBehaviours()` by checking `behaviour.data[currentLevel]` — use
  level 5 text for IC5+, level 2 text for everything below
- These are typically company values, kept verbatim

## Skills — the heart of the assessment

```javascript
const icSkills = [
  {
    name: 'Technical Depth',  // This name is used as the key for leadSupport and ratings
    data: {
      2: {
        signal: 'Can complete assigned technical tasks with guidance and explain their approach clearly.',
        bullets: [
          'Understands core concepts in the domain without needing to look everything up',
          'Identifies when a problem is outside their current capability and asks for help',
          'Reads and understands existing codebase / system documentation'
        ]
      },
      3: {
        signal: 'Independently solves moderately complex problems; colleagues seek their input on technical questions.',
        bullets: [
          'Designs simple systems or solutions without being told how',
          'Evaluates trade-offs between approaches and can explain the reasoning',
          'Contributes meaningfully in technical design discussions'
        ]
      },
      4: {
        signal: 'Leads technical decision-making for significant features; their technical judgment is trusted by senior engineers.',
        bullets: [
          'Makes architectural decisions within their area with confidence',
          'Identifies technical debt and proposes concrete remediation plans',
          'Reviews others\' technical work and provides substantive feedback'
        ]
      },
      5: {
        signal: 'Sets technical direction for a major system or area; their expertise shapes how the team solves problems.',
        bullets: [
          'Defines the technical strategy for their area 12+ months out',
          'Identifies cross-team technical dependencies before they become blockers',
          'Raises the technical bar of the team through mentoring and review'
        ]
      },
      6: {
        signal: 'Recognised externally as an authority; their technical judgments influence industry direction, not just internal decisions.',
        bullets: [
          'Drives technical innovation that creates competitive advantage',
          'Builds institutional knowledge that persists when people leave',
          'Defines what "senior engineering" looks like for the organisation'
        ]
      }
    }
  },
  // ... 5–8 more skills
];
```

**Notes on signal text:** This is the observable outcome — what does someone OUTSIDE the
person's team notice when they are "nailing it" at this level? Avoid "demonstrates" and
"shows" — use concrete, observable language.

**Notes on bullets:** 3–5 bullets of specific behaviours/activities. These show up in
the "focus on" section of goal cards.

## Lead support asks

```javascript
const icLeadSupport = {
  'Technical Depth': {
    1: 'Can you give me a structured way to build depth in [area]? I want to move from relying on you for answers to being the go-to person myself.',
    2: 'I want to take ownership of a technical problem end to end — something challenging enough to stretch me. What would you suggest?',
    3: 'I\'m looking to develop my ability to influence technical direction beyond my immediate team. How can you create visibility for me in the right conversations?'
  },
  // ... one entry per skill — names must match exactly
};
```

**Notes:** Ratings map: 1 = "not there yet", 2 = "getting there", 3 = "nailing it" (push
to next level). The key name must match `skill.name` exactly — it's used as a lookup.

## Timeframes — always declare this

```javascript
const icTimeframes = {1:'60 days', 2:'next quarter', 3:'3–6 months'};
```

## Career options

```javascript
const icCareerOptions = [
  {value: '',           label: 'Select where you\'re heading...'},
  {value: 'specialist', label: 'Go deep — become the expert in this function'},
  {value: 'people_lead',label: 'Move into people management'},
  {value: 'broader',    label: 'Broader product or business leadership role'},
  {value: 'startup',    label: 'Join or found an early-stage company'},
  {value: 'consulting', label: 'Consulting or advisory work'},
  {value: 'pivot',      label: 'Move into a different function entirely'},
  {value: 'own',        label: 'Build something of my own'},
  {value: 'unsure',     label: 'Not sure yet — still exploring'}
];
```

## Alignment data function

```javascript
function icGetAlignmentData(direction, level) {
  const nextLev = level < 6 ? icLevels[level+1] : null;
  const map = {
    specialist: {
      type: 'strong',
      icon: '🎯',
      title: 'Strong alignment — this track is built for you',
      body: `The IC track is designed for deep specialisation. Progressing to ${nextLev ? nextLev.code + ' ' + nextLev.title : 'IC6'} is a realistic, well-defined path.`,
      tips: [
        'Focus on your highest-priority gaps from this assessment first',
        'Start demonstrating Adaptive behaviours — that signals readiness to move up',
        'Document your impact in measurable terms'
      ]
    },
    people_lead: {
      type: 'partial',
      icon: '⚡',
      title: 'Mostly aligned — with one nuance to discuss',
      body: 'IC5 and IC6 already involve significant team influence and mentoring. Formal people management is a structural conversation for your lead.',
      tips: [
        'IC5/IC6 require developing others — lean into that now',
        'Have an explicit conversation with your lead about what people leadership means in this function',
        'The skills here make you a stronger manager regardless of structure'
      ]
    },
    // ... one entry per career option value
    unsure: {
      type: 'partial',
      icon: '🧭',
      title: 'That\'s fine — focus on getting excellent at this level first',
      body: 'Not knowing where you\'re heading is normal. Developing real depth at your current level will make the direction clearer.',
      tips: [
        'Notice which parts of the job energise you — that\'s data',
        'Have an honest conversation with your lead about what opportunities exist here',
        'Focus on skills that genuinely interest you, not just ones you think you should have'
      ]
    }
  };
  return map[direction] || map['unsure'];
}
```

**Alignment types:** `'strong'` (green tones), `'partial'` (amber), `'caution'` (red).
Be honest — not every direction deserves 'strong'.

---

## Active variables declaration — full block

```javascript
// ── ACTIVE TRACK DATA (swapped by setTrack) ──
let levels = icLevels;
let responsibilities = icResponsibilities;
let behaviours = icBehaviours;
let skills = icSkills;
let leadSupport = icLeadSupport;
let careerOptions = icCareerOptions;
let timeframes = icTimeframes;  // ← always include this one

let currentTrack = 'ic';
let currentLevel = null;
let currentView = 'browse';
let currentTab = 'responsibilities';
let assessStep = 1;
let ratings = {};
let notes = {};
let contextText = '';
let goalShort = '', goalMid = '', goalLong = '', careerDirection = '';
```

---

## Dual-track additions (IC + Manager)

When building a dual-track tool, add a track toggle bar between the header nav and the
level pills:

```html
<div class="track-toggle">
  <button class="track-btn active" onclick="setTrack('ic')" id="tbtn-ic">
    IC Track <span class="track-badge badge-ic">IC2–IC6</span>
  </button>
  <button class="track-btn" onclick="setTrack('manager')" id="tbtn-manager">
    Manager Track <span class="track-badge badge-mgr">M2–M7</span>
  </button>
</div>
```

And define all manager-track equivalents:
```javascript
const mgrLevels = { 2: {code:'M2', title:'Manager, [F]', badge:'Manager', badgeClass:'b-intermediate'}, ... };
const mgrResponsibilities = [...];
const mgrBehaviours = [...];
const mgrSkills = [...];
const mgrLeadSupport = {...};
const mgrCareerOptions = [...];
const mgrTimeframes = {1:'90 days', 2:'next quarter', 3:'3–6 months'};
```

Then `setTrack()` swaps all of them including `timeframes`.
