# Session Handoff — 2026-04-08

## Project
Linguistics-driven prompt compression benchmark and presentation materials in `/Users/francescawright/Documents/linguists_debate`.

## Goal of this session
1. Finish the incomplete benchmark output.
2. Replace the homemade caveman baseline with the real JuliusBrussee caveman skill variants.
3. Add repeat-run benchmarking via Codex.
4. Produce a clean presentation artifact summarizing methods, results, and value.
5. Capture new follow-on directions around agent-to-agent compressed communication.

## Status: COMPLETE FOR THIS PHASE

## What's done
- Updated `run_tests.py` to support both `claude` and `codex` runners with `--runner`.
- Added `--output`, `--timeout`, `--repeats`, and `--baseline` flags to `run_tests.py`.
- Replaced the toy caveman prompt with three real baseline variants based on JuliusBrussee/caveman:
  - `caveman_real_lite`
  - `caveman_real_full`
  - `caveman_real_ultra`
- Switched the benchmark default baseline to `caveman_real_full`.
- Reworked reporting so repeated runs are averaged and individual run word counts are shown.
- Ran the full benchmark with Codex:
  - command used: `python3 run_tests.py --runner codex --repeats 3`
- Regenerated `test_results.md` from that run.
- Confirmed the current winner on output length is `round3`, now presented as:
  - `Minimal Semantic Compression (Round 3)`
- Built a presentation artifact:
  - `benchmark_report.html`
- Iteratively expanded the HTML report to include:
  - summary findings
  - visual bar charts
  - representative examples
  - methodology
  - debate-results-by-method summary
  - linguistics behind each method
  - estimated output-cost section framed as “this would have cost X vs Y”
  - session-scale / workload-scale extrapolation
  - compact next-steps box
- Renamed methods in the report for presentation clarity while retaining round traceability:
  - Overhead Elimination (Round 1)
  - Structural Compression (Round 2)
  - Minimal Semantic Compression (Round 3)
  - Judge Integration (Round 4)

## Current benchmark result
Using `caveman_real_full` as baseline, repeated Codex run:

- `caveman_real_full`: `657`
- `caveman_real_ultra`: `533.3`
- `round1`: `532`
- `round2`: `307.7`
- `round3`: `272`
- `round4_final`: `356`

Current winner:
- `Minimal Semantic Compression (Round 3)`
- about `58.6%` shorter than `caveman_real_full` on current output-length benchmark

Important caveat:
- this is an output-length benchmark, not yet true total-token accounting
- this was run on Codex, not yet rerun on Claude after the runner upgrade

## Key decisions
- Reframe the work as `linguistically informed prompt compression`, not “AI debate discovers truth.”
- Treat the debate system as the ideation/generation engine and the benchmark as the evidence layer.
- Use the real JuliusBrussee caveman skill as the serious baseline, not a homemade caveman-style prompt.
- Keep `round` labels in code and raw files, but present publishable method names in the report.
- Present cost savings as comparative estimated spend (`X vs Y`) rather than abstract token savings only.

## Files touched this session
- `/Users/francescawright/Documents/linguists_debate/run_tests.py`
- `/Users/francescawright/Documents/linguists_debate/test_results.md`
- `/Users/francescawright/Documents/linguists_debate/benchmark_report.html`

## New ideas discussed but not implemented

### 1. Small refinement to Method 3
Likely next prompt refinement:
- add a one-word rule for atomic factual queries

Why:
- Method 3 currently loses only on the simple one-word factual case
- this looks like the clearest surgical fix

### 2. Debate UI as portfolio artifact
Idea:
- present debates in a simple Telegram-style chat interface
- one speaker at a time
- slight delay / “typing” effect
- visible disagreement followed by synthesis and benchmark result

Why it matters:
- strong portfolio presentation
- shows research framing + product presentation + system thinking
- the interface can be basic; the value is clarity and narrative

Recommended framing:
- debate = ideation layer
- benchmark = validation layer

### 3. Agent-to-agent compressed communication / proto-language
Promising follow-on subproject:
- instead of only compressing final user-facing answers, compress agent-to-agent communication itself

Core idea:
- agents do not need full natural-language English to coordinate internally
- they need compact, reliable transfer of claims, objections, evidence, confidence, and next actions

Recommended framing:
- “compressed coordination protocol”
- or “machine-oriented coordination grammar”
- “proto-language” is good as a conceptual label, but pair it with a more concrete technical description

Initial design direction:
- do not invent a freeform language
- use a constrained protocol with tiny vocabulary and fixed slots

Example style:
```text
CLAIM: drop framing
EVID: q2,q3 shorter
OBJ: q1 factual loss
FIX: one-word rule for atomic facts
CONF: medium
NEXT: rerun benchmark
```

This is likely better than open-ended compressed prose because it is:
- cheaper
- more parseable
- easier to validate
- easier to translate back to English

## Risks identified for the proto-language idea
- protocol becomes too cryptic and loses reliability
- agents drift back into prose or inconsistent formatting
- savings are erased by repair traffic
- debugging gets harder than the token savings are worth

## Suggested safeguards for that proto-language work
- keep vocabulary tiny
- use fixed message types and fixed fields
- allow a plain-English fallback / `ESCALATE`
- validate messages structurally
- benchmark protocol compliance, repair rate, and net token savings
- keep it as controlled English rather than a pure symbolic language, at least initially

## Best next steps
1. Run the upgraded benchmark on Claude when available again:
   - `python3 run_tests.py --runner claude --repeats 3`
2. Add the one-word factual rule to Method 3 and compare against current Round 3.
3. Expand the benchmark from 6 queries to 50-100 balanced queries.
4. Add quality scoring, not just output length:
   - correctness
   - completeness
   - usefulness
   - safety
5. Measure real API token accounting and latency, not just word counts.
6. If portfolio presentation is the next priority, build a lightweight Telegram-style replay UI for the debates.
7. If research novelty is the next priority, spin up the compressed agent-coordination protocol as a separate experiment.

## How to resume
- Open `/Users/francescawright/Documents/linguists_debate/benchmark_report.html` for the current polished summary.
- Open `/Users/francescawright/Documents/linguists_debate/test_results.md` for the raw benchmark outputs.
- Open `/Users/francescawright/Documents/linguists_debate/run_tests.py` for the benchmark harness.
- Decide whether the next task is:
  - Claude rerun
  - Method 3 refinement
  - larger benchmark set
  - Telegram-style debate UI
  - compressed agent-coordination protocol
