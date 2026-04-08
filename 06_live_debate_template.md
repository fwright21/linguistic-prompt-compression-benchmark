# Live Debate Template

Use this template for each new debate round. Copy it, rename the copy with the round number, and fill it in.

---

## Round metadata

**Round number:**
**Agents:**
**Date:**
**Benchmark query used in examples:**
**Caveman baseline response and token count:**

---

## Part 1 — Opening Statements

Each agent answers: what system prompt instruction produces the shortest coherent Claude output? Concrete claim. Actual instruction text. No hedging.

### [Agent 1]

[Opening statement — include one-sentence instruction at the end]

---

### [Agent 2]

[Opening statement — include one-sentence instruction at the end]

---

### [Agent 3]

[Opening statement — include one-sentence instruction at the end]

---

### [Agent 4]

[Opening statement — include one-sentence instruction at the end]

---

## Part 2 — Cross-Examination

At least 2 genuine clashes. A clash is where two agents have incompatible claims about what can be dropped without losing coherence or recoverability.

### Clash 1: [Agent X] vs. [Agent Y] — [Conflict in one phrase]

**[Agent X] challenges [Agent Y]:**

[Challenge — identify specifically what the other agent is wrong about]

**[Agent Y] responds:**

[Response — defend or concede]

**Resolution:** [What was conceded? What held?]

---

### Clash 2: [Agent X] vs. [Agent Y] — [Conflict in one phrase]

**[Agent X] challenges [Agent Y]:**

[Challenge]

**[Agent Y] responds:**

[Response]

**Resolution:** [What was conceded? What held?]

---

## Part 3 — Revised Positions

Each agent updates their position. If unchanged, state "Position held" and explain why cross-examination did not change it.

**[Agent 1] (revised):**

**[Agent 2] (revised):**

**[Agent 3] (revised):**

**[Agent 4] (revised):**

---

## Part 4 — Draft System Prompts

Each agent produces actual system prompt text. 2-6 sentences. Ready to paste. No descriptions — the prompt itself.

### [Agent 1]'s draft
> [Prompt text]

### [Agent 2]'s draft
> [Prompt text]

### [Agent 3]'s draft
> [Prompt text]

### [Agent 4]'s draft
> [Prompt text]

---

## Part 5 — Synthesis

**Ideas that survived cross-examination:**

| Claim | Proposed by | Survived because |
|-------|-------------|-----------------|
| | | |

**Ideas that did not survive:**

| Claim | Proposed by | Why it failed |
|-------|-------------|---------------|
| | | |

### Round [N] Candidate System Prompt

> [Actual prompt text — ready to use]

---

## Simulated outputs

**Query:** [Benchmark query]

**Caveman output:**
> [Output]
Estimated tokens: [N]

**Candidate output:**
> [Output]
Estimated tokens: [N]

**Token delta:** [+/- N tokens vs. caveman]

**Assessment:** [Does the candidate beat caveman on this query? Where does it win and lose?]
