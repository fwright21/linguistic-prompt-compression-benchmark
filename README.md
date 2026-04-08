# Linguists Debate: Beat the Caveman

This repo stages a debate between major linguists (Chomsky, Pinker, Lakoff, and others) to design a prompt-compression method that beats caveman, using minimal linguistic principles to reduce output length without losing usefulness.

## Quick Summary

- Progress: debate rounds completed, benchmark harness upgraded, 60-query dataset prepared, and Codex baseline run completed.
- Current best evidence: `Minimal Semantic Compression (Round 3)` is `+58.6%` shorter than `caveman_real_full` on the completed 6-query Codex benchmark (`272` vs `657` total avg words).
- Why this is better than a generic caveman prompt: prompt rules are linguistically motivated and systematically benchmarked, not ad-hoc style instructions.
- What is still pending: Claude rerun on the expanded set and formal quality scoring (DeepEval-style rubric evaluation).

## Project Status (as of 2026-04-08)

- Debate rounds complete (Rounds 1-4)
- Codex benchmark run complete on the original 6-query suite (`--repeats 3`)
- Expanded benchmark set prepared (60 queries, category-balanced)
- Claude rerun pending (blocked by token credits)
- Quality scoring pipeline (DeepEval-style) planned, not implemented yet

## Best Result So Far

From `test_results.md` (Codex runner, 6-query suite, 3 repeats, baseline `caveman_real_full`):

- `caveman_real_full`: `657` avg words total
- `Minimal Semantic Compression (Round 3)`: `272` avg words total
- Improvement: `+58.6%` shorter than baseline

Current winner: `Minimal Semantic Compression (Round 3)`.

Important caveat:
- this result is output-length only (word-count proxy)
- this is not yet validated on Claude
- this does not yet include formal quality metrics

## Real Caveman Baselines Used

This project no longer uses the toy baseline line (`"You are a caveman..."`).
It uses three variants adapted from JuliusBrussee/caveman and encoded in `run_tests.py`:

- `caveman_real_lite`
- `caveman_real_full` (default baseline)
- `caveman_real_ultra`

Reference:
- https://github.com/JuliusBrussee/caveman

## Methodology

The process has two layers:

1. ideation layer: linguist-agent debates generate prompt candidates from explicit linguistic principles
2. evidence layer: repeated benchmark runs measure response-length outcomes against the caveman baseline

Named methods:

- `Overhead Elimination (Round 1)`
- `Structural Compression (Round 2)`
- `Minimal Semantic Compression (Round 3)`
- `Judge Integration (Round 4)`

Method naming is intentional: the repo keeps round traceability while presenting each candidate as a reusable compression strategy.

## Benchmark Harness

Main script: `run_tests.py`

Key features:
- supports `codex` and `claude` runners (`--runner`)
- repeat runs (`--repeats`)
- configurable baseline (`--baseline`)
- external query set via JSONL (`--queries`)
- per-query + per-category summaries in markdown output

Current query set:
- `benchmark_queries.jsonl`
- 60 total queries
- categories: factual, definition, comparison, procedure, recommendation, ambiguous, safety_sensitive, numerical_reasoning
- per-query metadata: `expected_traits`, `rubric_focus`

## Run Commands

Smoke run:

```bash
python3 run_tests.py --runner codex --repeats 1 --output test_results_codex_smoke.md
```

Full Codex run:

```bash
python3 run_tests.py --runner codex --repeats 3 --output test_results_codex.md
```

Full Claude run (pending credits):

```bash
python3 run_tests.py --runner claude --repeats 3 --output test_results_claude.md
```

## Results Artifacts

- `test_results.md` - latest completed benchmark output
- `benchmark_report.html` - presentation/report view of findings
- `run_tests.py` - benchmark harness
- `benchmark_queries.jsonl` - benchmark dataset

## Next Steps

1. Run full 60-query benchmark on Claude.
2. Re-run Codex on the 60-query set for apples-to-apples comparison.
3. Add quality scoring (correctness, completeness, usefulness, safety).
4. Integrate DeepEval (or equivalent) for rubric-based automated evaluation.
5. Report combined metric: compression + quality (quality-adjusted compression).

## File Map

- `00_debate_method.md` - debate mechanics
- `01_linguist_agents.md` - linguist personas and prompts
- `02_shared_questions.md` - shared agent prompts
- `03_synthesis_template.md` - synthesis structure
- `04_better_than_caveman_criteria.md` - evaluation criteria
- `05_round_one_debate.md` - Round 1 transcript
- `06_live_debate_template.md` - template for new rounds
- `07_live_run_mode.md` - live run guidance
- `08_round_two_debate.md` - Round 2 transcript
- `09_final_proposal.md` - synthesis proposal
- `10_benchmark_suite.md` - original benchmark framing
- `11_benchmark_cases.md` - benchmark case development
- `12_benchmark_results_template.md` - result template
- `13_round_three_agents.md` - Round 3 setup
- `14_round_three_debate.md` - Round 3 transcript
- `proposals.md` - proposal leaderboard
