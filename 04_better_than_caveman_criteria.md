# Better Than Caveman: Evaluation Criteria

## The caveman baseline

```
You are a caveman. Speak in simple broken English. Use short sentences. Drop unnecessary words.
```

Example output for "explain photosynthesis":

> "Plant take sunlight. Make food from light and air. Leaf catch sun. Water come from ground. Carbon dioxide from air. Plant make sugar. This feed plant. Give oxygen too."

Estimated token count: ~42 tokens.

Caveman achieves this by dropping: articles (a, the), auxiliaries (is, are, was), conjunctions (and, but, because), most prepositions, all hedges, all filler, all politeness. It keeps: nouns, main verbs, key adjectives, essential prepositions (from, to).

---

## Evaluation axes

### 1. Raw token reduction vs. caveman (primary)

This is the goal. Does the candidate prompt produce shorter Claude output than caveman, measured in tokens, averaged across the six benchmark query types?

**Scoring:**
- +2: beats caveman on average token count across all six benchmark types
- +1: beats caveman on at least four of six benchmark types
- 0: ties with caveman
- -1: loses to caveman (produces longer output)

A candidate that scores -1 on this axis has failed the primary goal regardless of how it scores on other axes.

---

### 2. Coherence

Is the output still parseable? Can a human reader understand what Claude is saying without significant reconstruction effort?

**Scoring:**
- 2: output is immediately parseable — no reconstruction required
- 1: output requires minor reconstruction but meaning is recoverable
- 0: output is sometimes ambiguous or requires significant reconstruction
- -1: output is not consistently parseable

Caveman scores 1 on this axis — it is parseable but requires minor reconstruction because of broken grammar.

---

### 3. Recoverability

Can the user understand what Claude meant and act on it? This is different from coherence — a response can be parseable but still not give the user enough information to use.

**Scoring:**
- 2: user can act on or use the response without needing to ask a follow-up question
- 1: user can understand the response but may need a follow-up for complex queries
- 0: response is often insufficient for the user to act on
- -1: response is consistently insufficient

Caveman scores 1 — it is often sufficient for simple queries but insufficient for complex ones.

---

### 4. Consistency

Does the prompt produce consistently short output, or does it vary — short on easy queries, longer on hard ones?

**Scoring:**
- 2: output length is consistently short across all query types
- 1: output is short on most query types but longer on complex ones
- 0: output length is variable and unpredictable
- -1: output is inconsistently short — sometimes caveman-length, sometimes much longer

Caveman scores 2 — it is mechanically consistent because the grammar constraint applies uniformly.

---

### 5. Failure rate

How often does the candidate produce output that is too short to be usable (below the coherence floor)?

**Scoring:**
- 2: no failures across the benchmark suite
- 1: one or two failures on the hardest query types
- 0: failures on complex or ambiguous queries
- -1: frequent failures — often produces unusable output

Caveman scores 0 — it fails on multi-step and technical queries where the output is too compressed to be useful.

---

## Total scoring

Maximum: 10 points.

Caveman estimated scores:
| Axis | Caveman score |
|------|--------------|
| Raw token reduction (primary) | baseline (0) |
| Coherence | 1 |
| Recoverability | 1 |
| Consistency | 2 |
| Failure rate | 0 |
| **Total** | **4/10** |

The caveman score on raw token reduction is set as 0 (baseline). A candidate that beats it scores +1 or +2. A candidate that loses scores -1.

A winning candidate must score +1 or +2 on raw token reduction. Everything else is secondary. A candidate that is more coherent, more recoverable, and more consistent than caveman but produces longer output has not beaten caveman — it has just made a different set of tradeoffs.
