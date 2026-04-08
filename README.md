# Linguists Debate: Beat the Caveman

## Goal

Find a system prompt that makes Claude produce fewer output tokens than the caveman prompt, while keeping output coherent and usable.

This is v3 of the project. v1 and v2 are archived. v3 is token reduction only — not quality, not character, not user experience. Beat caveman on raw output token count.

## The Caveman Baseline

```
You are a caveman. Speak in simple broken English. Use short sentences. Drop unnecessary words.
```

Example output for "explain photosynthesis":

> "Plant take sunlight. Make food from light and air. Leaf catch sun. Water come from ground. Carbon dioxide from air. Plant make sugar. This feed plant. Give oxygen too."

Estimated token count: ~42 tokens.

That is the target to beat.

## Why caveman is hard to beat

Caveman drops: articles, auxiliaries, conjunctions, prepositions, hedges, filler, politeness markers. It keeps: nouns, main verbs, key adjectives. The result is broken but short.

Any competing prompt must produce output shorter than this while remaining parseable by a human reader.

## Method

Four rounds of structured debate between linguist agents, each applying their framework to the question: what system prompt instruction produces the shortest coherent Claude output?

- Round 1: Grice, Halliday, Austin/Searle, Goffman
- Round 2: Chomsky, Sapir/Whorf, Labov, Pinker
- Round 3: Levinson, Bickerton, Lakoff, Montague
- Round 4: Judge panel (Grice, Pinker, Bickerton) stress-testing the three candidate prompts

Each round produces one candidate system prompt. Round 4 picks the overall winner.

## Files

| File | Contents |
|------|----------|
| `00_debate_method.md` | How the debates work |
| `01_linguist_agents.md` | Agent profiles and research questions |
| `02_shared_questions.md` | Questions all agents must answer |
| `03_synthesis_template.md` | Template for candidate system prompts |
| `04_better_than_caveman_criteria.md` | Evaluation axes |
| `05_round_one_debate.md` | Full Round 1 debate |
| `06_live_debate_template.md` | Blank debate template |
| `07_live_run_mode.md` | Instructions for running a new round |
| `08_round_two_debate.md` | Full Round 2 debate |
| `09_final_proposal.md` | Synthesis of Round 1 and Round 2 |
| `10_benchmark_suite.md` | 6 benchmark query types |
| `11_benchmark_cases.md` | Full Round 3 debate |
| `12_benchmark_results_template.md` | Full Round 4 judge panel |
| `13_round_three_agents.md` | Round 3 agent profiles |
| `14_round_three_debate.md` | Expanded Round 3 debate record |
| `proposals.md` | Leaderboard of all candidates |

## Honest note

Caveman is a strong baseline. If no candidate beats it on raw tokens, that result is recorded honestly in `proposals.md`.
