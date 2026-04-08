# Debate Method

## Purpose

Find a system prompt that produces shorter Claude output than caveman. Not better output. Shorter output, measured in tokens, while remaining coherent and usable.

The caveman prompt is the competitor. It is not a straw man. It produces output that is extremely short because it drops articles, auxiliaries, conjunctions, prepositions, hedges, and filler while keeping nouns, main verbs, and key adjectives. Any candidate must beat its token count while producing output a human can still parse and use.

---

## The core question for every round

> What system prompt instruction produces the shortest coherent Claude output?

Every agent must answer this question with actual candidate system prompt text. Theoretical claims without prompt-text implications are not accepted.

---

## Four rounds

### Round 1 — Pragmatics agents
Agents: Grice, Halliday, Austin/Searle, Goffman

These frameworks ask: which elements of communication are necessary for the message to function? Anything unnecessary is a token that can be dropped. Round 1 agents identify what caveman drops that turns out to be necessary, and what caveman keeps that could also be dropped.

Full debate in `05_round_one_debate.md`.

### Round 2 — Structure and cognition agents
Agents: Chomsky, Sapir/Whorf, Labov, Pinker

These frameworks ask: what is the minimum syntactic and cognitive structure a response needs to be recoverable? Chomsky asks about minimum syntax. Pinker asks about minimum viable explanation. Labov asks about narrative overhead. Sapir/Whorf asks about unnecessary distinctions Claude encodes.

Full debate in `08_round_two_debate.md`.

### Round 3 — Formal and contextual agents
Agents: Levinson, Bickerton, Lakoff, Montague

These frameworks ask: what can Claude leave unsaid because context carries it? What is the creole minimum? Which conceptual framings bloat token count? Which semantic components are redundant given what the user already knows?

Full debate in `11_benchmark_cases.md`.

### Round 4 — Judge panel
Agents: Grice, Pinker, Bickerton

This round stress-tests the three candidate system prompts from Rounds 1, 2, and 3. Judges simulate what Claude would output under each candidate prompt, estimate token counts, compare to caveman, identify failure cases, and pick the overall winner.

Full debate in `12_benchmark_results_template.md`.

---

## Structure of each debate round

1. **Opening statements** — each agent's answer to the core question. Concrete claim. What instruction produces shorter output and why.
2. **Cross-examination** — at least 2 genuine clashes. One agent challenges another's claim. Challenged agent responds.
3. **Revised positions** — each agent updates their position after cross-examination.
4. **Draft system prompts** — each agent produces actual candidate prompt text, 2-6 sentences, ready to paste into a system prompt field.
5. **Synthesis** — which ideas survived? What is the round's candidate system prompt?

---

## After four rounds

The three candidate system prompts (Rounds 1, 2, 3) go to the Round 4 judge panel. Judges simulate outputs, estimate token counts, pick the winner. The final candidate and an honest assessment of whether it beats caveman are recorded in `proposals.md`.

---

## Rules

- All candidate system prompts must be plain English. No notation, no codes.
- Caveman must be named as the baseline competitor in every synthesis.
- Claims about token reduction must be grounded in simulated outputs against the benchmark suite (`10_benchmark_suite.md`).
- If no candidate beats caveman on raw token count, that result must be stated honestly.
- Coherence is the floor: output that cannot be parsed and used is disqualified regardless of token count.
