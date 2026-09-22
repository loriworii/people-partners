# Tactical + Adaptive Framework — Content Writing Guide

## The framework in one paragraph

Neel Doshi distinguishes between two types of performance that every role requires:
- **Tactical performance**: convergent, execute reliably, follow the playbook well. This is the baseline.
  Without it, nothing ships.
- **Adaptive performance**: divergent, go beyond the brief, improve the system, respond to what wasn't
  anticipated. This is what separates a good performer from an exceptional one.

A career path built on this framework makes the distinction visible at every level. It answers two
different questions simultaneously: "Are you doing the job?" (Tactical) and "Are you evolving the
job?" (Adaptive). The Ownership statement anchors accountability. The Impact line closes the loop.

---

## Cell structure for responsibility domains

Every responsibility cell must follow this exact structure:

```
Ownership: [Who owns what — a complete sentence that names the scope and stakes clearly]

Tactical (Execute):
* [What must be done reliably — concrete, specific, completable]
* [...]
* [...]

Adaptive (Evolve):
* [Where to go beyond the brief — identifies a gap, an improvement, or a new frontier]
* [...]
* [...]

Impact: [What good looks like as an observable outcome — one sentence]
```

Python helper:
```python
def fmt(ownership, tactical, adaptive, impact):
    t  = f"Ownership: {ownership}\n\n"
    t += "Tactical (Execute):\n"
    for b in tactical: t += f"* {b}\n"
    t += "\nAdaptive (Evolve):\n"
    for b in adaptive: t += f"* {b}\n"
    t += f"\nImpact: {impact}"
    return t.strip()
```

---

## Writing the Ownership statement

The Ownership statement defines what this person is accountable for — not what they do, but what
they hold. It should answer: "If this goes wrong, whose fault is it?"

**IC tracks**: Ownership escalates from "you own execution of assigned tasks" → "you own a domain
or functional area" → "you own the function's strategic output and reputation".

**Manager tracks**: Ownership escalates from "you own your team's output and development" → "you
own the function's capability and culture" → "you own the function's strategic contribution to
the company".

**Anti-patterns to avoid**:
- ❌ "You are responsible for doing X and Y and Z" — this is a task list, not an ownership statement
- ❌ "Ownership: Supporting the team" — support is not ownership
- ✅ "You own the analytical quality and strategic relevance of your domain. You are expected to
  lead projects end-to-end and be the analytical authority for your functional area."

---

## Writing Tactical bullets

Tactical bullets are the non-negotiable baseline. If someone isn't doing these, they are not
performing at this level. They should be:
- Specific and completable (not aspirational)
- Grounded in the actual work of the function (reference tools, processes, stakeholders where relevant)
- Broadly similar in spirit across levels, but escalating in scope and autonomy

**The escalation pattern across levels**:
- IC2: does it under supervision → IC3: does it independently → IC4: leads it → IC5: defines the
  standard for it → IC6/IC7: shapes how the organisation thinks about it

**Anti-patterns**:
- ❌ "Demonstrates strong analytical skills" — describes a trait, not an activity
- ❌ "Works with stakeholders" — too vague
- ✅ "Partner directly with product managers, marketers, and finance teams to answer their analytical
  questions before they ask"

---

## Writing Adaptive bullets

This is where the real differentiation between levels lives. Adaptive bullets describe what a high
performer at this level does that goes beyond reliable execution — the improvements, the proactive
moves, the reframing of problems.

**Key tests for a good Adaptive bullet**:
1. Could a solid performer at the level below also do this? If yes, it's not Adaptive enough.
2. Is it about improving the system, not just performing within it?
3. Does it describe a behaviour or move that requires judgment — not just diligence?

**Common Adaptive patterns by level**:
- Early levels: "Notice and flag" (proactively surface problems before being asked)
- Mid levels: "Build and improve" (create things that outlast the current campaign/project)
- Senior levels: "Shape and anticipate" (define how the organisation approaches a problem before
  the problem arrives)
- Exec levels: "Reframe the game" (change what success looks like, influence external landscapes)

**Anti-patterns**:
- ❌ "Go above and beyond" — says nothing
- ❌ Adaptive bullets that are just more Tactical bullets
- ✅ "Identify where the organisation's analytical priorities are misaligned with business value
  and reorient them — before anyone asks"

---

## Writing the Impact statement

One sentence. What does good look like as an observable outcome? Not an activity, not a behaviour —
a result.

**Escalation pattern**:
- IC2: individual/team reliability ("Reliable, well-documented work that teams can trust")
- IC3: team decisions ("Insights that directly improve decisions within your team or domain")
- IC4/IC5: cross-team or function-level impact ("Analytical work that influences product roadmaps")
- IC6/IC7: company or industry-level ("Transforms how the company uses data to operate and compete")

---

## Cell structure for skills domains

```
* [Bullet from existing skills content]
* [...]
* [...]

Observable signal: [A specific, verifiable behaviour that proves the skill is present]
```

Python helper:
```python
def skl(bullets, signal):
    return "\n".join(f"* {b}" for b in bullets) + f"\n\nObservable signal: {signal}"
```

**Writing Observable Signals**:

The signal should be something a manager or HR partner could actually observe or verify in a
calibration discussion — not a trait, not a vague description.

**Good signals**:
- "Produces a dashboard that a non-technical stakeholder can interpret correctly without follow-up —
  validated by stakeholder feedback"
- "A journalist at a target outlet reaches out proactively for a comment — evidence that a genuine
  relationship, not just a contact, has been built"
- "Leads a crisis response that is later assessed positively by leadership — no message drift,
  no uncoordinated media interactions, clear post-crisis review completed"

**Bad signals**:
- "Demonstrates strong communication skills" — a trait
- "Communicates clearly with stakeholders" — describes the behaviour but can't be verified
- "Consistently meets deadlines" — too generic, not skill-specific

The signal should be the kind of evidence you would cite in a promotion case or a calibration
discussion. It makes assessment transparent rather than leaving it to subjective interpretation.

---

## Level progression — the key principle

When reviewing a draft, read just the Adaptive section from IC2 through IC7 (or M2 through M7).
If those bullets feel like a gradual escalation of the same activity, you need to rewrite.

Good level progression creates qualitatively different operating modes:
- **IC2**: responds to requests → **IC3**: anticipates follow-up → **IC4**: shapes how questions
  are framed → **IC5**: changes what questions get asked → **IC6**: defines the measurement standard
  → **IC7**: shapes how the industry thinks about it

The question is not "how much more?" but "in what different way?"

---

## Specificity is quality

Generic content is weak content. Career paths that could apply to any company at any industry
feel like HR boilerplate — managers ignore them, employees don't trust them.

Make it specific:
- Name the tools: not "analytics platforms" but "dbt, Looker, Snowflake"
- Name the channels: not "media" but "CoinDesk, The Block, Decrypt, Blockworks"
- Name the audiences: not "stakeholders" but "product managers, the CMO, the CTO, ecosystem partners"
- Name the context: not "industry trends" but "DeFi mechanics, Layer 2 dynamics, regulatory
  trajectories, on-chain data"
- Name the products: not "our products" but "MetaMask, Linea, Infura"

If you don't have this context from the user, ask for it in Step 1. The specificity is the point.

---

## Behaviours — never change them

If the user provides existing behaviours (in a source file or described in the brief), copy them
verbatim. Do not rephrase for clarity, do not fix grammatical quirks, do not update terminology.

Why: The behaviours have typically been through a review process with legal, leadership, or the
broader team. They are considered "done". Changing them introduces risk the user hasn't asked for.

If there are no existing behaviours, use the standard two-tier set:
- Lower tier (IC2–IC4 or equivalent): "approach, participate, provide/accept feedback" language
- Upper tier (IC5+ or all managers): "lead, model, cultivate, drive" language

Standard behaviours (lower tier):
```
We act with kindness:
* Treat others with care, compassion, and dignity in daily interactions.
* Regularly check in on team members and provide thoughtful, empathetic feedback.
* Foster inclusivity and belonging by listening deeply and understanding diverse perspectives.
* Collaborate with transparency, consulting with impacted stakeholders before making decisions.

We cultivate community:
* Support and empower team members by leveraging each other's strengths to achieve goals.
* Actively participate in team efforts, contributing to open, inclusive decision-making.
* Recognise and value diversity in the workplace, fostering collaboration across different backgrounds.
* Build partnerships with internal and external stakeholders to align with shared goals.

We continually evolve:
* Approach all projects with a growth mindset, learning from mistakes and seeking continuous improvement.
* Provide and accept feedback openly, encouraging personal and team development.
* Embrace change and actively seek new learning opportunities to refine your skills and knowledge.
* Work with agility, adapting quickly to new insights or data from the market or team.

We embrace innovation:
* Encourage creative problem-solving by seeking diverse opinions and exploring new solutions.
* Actively contribute to innovative discussions, asking questions and sharing knowledge with the team.
* Adapt to changes and emerging technologies, staying agile in your work approach.
* Participate in experimentation and continuous improvement to drive team innovation.

We deliver impact:
* Set clear objectives for your work, ensuring alignment with team and company goals.
* Follow through on commitments and be accountable for delivering high-quality results.
* Identify opportunities to deliver impactful outcomes through collaboration and thoughtful planning.
* Participate in swift, collective decision-making that drives progress.
```

Standard behaviours (upper tier):
```
We act with kindness:
* Proactively lead initiatives that promote kindness and empathy within the team.
* Mentor junior team members, modelling a culture of compassion and authentic communication.
* Ensure transparency and inclusiveness in decision-making, involving relevant stakeholders.
* Advocate for a supportive and caring community, recognising achievements and contributions.

We cultivate community:
* Take ownership of cultivating a strong team culture, emphasising collective success over individual achievement.
* Lead cross-functional collaborations that harness diverse expertise for innovative solutions.
* Drive inclusive decision-making processes that respect and integrate diverse perspectives.
* Build strategic partnerships with key internal and external stakeholders to further team and company goals.

We continually evolve:
* Lead by example, modelling continuous learning and development within the team.
* Proactively solicit and integrate diverse feedback to drive team evolution.
* Guide the team through changes, leveraging market insights to continuously refine strategies.
* Mentor others in adopting a growth mindset, fostering a culture of iteration and learning.

We embrace innovation:
* Drive innovative projects, fostering a culture of curiosity and creative thinking.
* Proactively lead teams through experimentation and agile development processes.
* Advocate for new technologies and processes that will enable the team to stay ahead of industry trends.
* Inspire others to embrace change and position the team at the forefront of innovation.

We deliver impact:
* Lead strategic initiatives that deliver significant impact, driving team and company success.
* Ensure the team sets measurable goals and is accountable for delivering exceptional outcomes.
* Align resources and efforts toward delivering high-quality strategies and solutions.
* Evaluate results rigorously, iterating processes and strategies to improve impact continuously.
```
