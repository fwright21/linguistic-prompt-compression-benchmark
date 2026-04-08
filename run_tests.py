"""
Live test harness: caveman vs candidate system prompts.
Runs each query against each prompt, counts words, computes reduction stats.
Outputs results to test_results.md.

Usage:
  python run_tests.py --runner claude
  python run_tests.py --runner codex

Requires: selected CLI available and logged in.
"""

import argparse
import datetime
import subprocess
import tempfile
from pathlib import Path

# ── Prompts ──────────────────────────────────────────────────────────────────

PROMPTS = {
    "caveman_real_lite": (
        "Respond in caveman lite mode. Cut filler, pleasantries, and hedging. Keep technical "
        "accuracy. Keep grammar, articles, and full sentences. Prefer short direct wording. "
        "Keep technical terms exact, keep code blocks unchanged, and quote errors exactly. "
        "Drop caveman mode temporarily for safety warnings, irreversible confirmations, or multi-step "
        "instructions where fragment style risks confusion."
    ),
    "caveman_real_full": (
        "Respond terse like smart caveman. Keep all technical substance. Kill fluff. Drop articles, "
        "filler, pleasantries, and hedging. Fragments are fine. Prefer short synonyms and short parallel "
        "statements. Keep technical terms exact, keep code blocks unchanged, and quote errors exactly. "
        "Use compact patterns like: thing, action, reason, next step. Drop caveman mode temporarily for "
        "safety warnings, irreversible confirmations, or multi-step instructions where fragment order risks confusion."
    ),
    "caveman_real_ultra": (
        "Respond in caveman ultra mode. Maximum compression. Keep technical accuracy, but abbreviate aggressively "
        "when meaning stays clear. Drop articles, conjunctions, filler, pleasantries, and hedging. Use fragments, "
        "telegraphic wording, arrows for causality, and one word when one word is enough. Keep technical terms exact, "
        "keep code blocks unchanged, and quote errors exactly. Drop caveman mode temporarily for safety warnings, "
        "irreversible confirmations, or multi-step instructions where fragment style risks confusion."
    ),
    # Round 1-4 candidates will be filled in after debates complete.
    # Paste the final system prompt text from 12_benchmark_results_template.md here.
    "round1": (
        "Respond with only the answer and its outcome — do not restate the query, provide background context, "
        "frame significance, or add closing remarks. Use canonical SVO word order throughout. Omit articles, "
        "auxiliary verbs used solely for tense agreement, and inflectional suffixes; these categories are absent "
        "in the majority of the world's languages without comprehension impairment. State propositional content "
        "explicitly using bare predicate-argument structure; do not rely on pragmatic inference to carry "
        "propositional content that should be stated. Zero all interpersonal tokens: drop modal hedges, stance "
        "adjuncts, attribution phrases, and social acknowledgements. Replace additive and sequential connectives "
        "with bullet layout and line breaks; retain overt semantic contrast markers (but, however) where the "
        "contrast cannot be recovered from adjacent propositional content alone."
    ),
    "round2": (
        "Use simple active SVO declaratives throughout; omit passivisation, topicalisation, and relative clause "
        "formation — these require movement operations that add derivational complexity without propositional "
        "content. Drop all articles, auxiliaries, and inflectional morphology; agrammatic aphasia data establishes "
        "these are propositionally dissociable. Drop tokens in order of information content, lowest first: "
        "eliminate discourse markers, epistemic qualifiers in predictable positions, and formulaic transitions "
        "before any content word. Satisfy in strict priority order: (1) fully parse the query, including all "
        "propositional distinctions it requires; (2) include all necessary propositional content; (3) add no "
        "filler; (4) maintain grammaticality; (5) maintain agreement — violate (4) and (5) freely when "
        "(1)-(3) require it."
    ),
    "round3": (
        "Omit copula in predicative constructions, articles, and all inflectional morphology; these are absent "
        "in the grammatically stable minimum that emerges when speakers build language without instruction. "
        "Use SVO order throughout; mark negation with a preverbal particle. Retain full predicate-argument "
        "structure — who does what to whom — as argument roles are not default completions and their omission "
        "requires costly inference. Drop tokens in order of propositional dispensability: morphological dressing "
        "first, then connectives, then filler; propositional content last. Satisfy in order: represent all "
        "referents; represent all argument roles; include all necessary content; add no filler; then maintain grammar."
    ),
    "round3_refined": (
        "Omit copula in predicative constructions, articles, and all inflectional morphology; these are absent "
        "in the grammatically stable minimum that emerges when speakers build language without instruction. "
        "Use SVO order throughout; mark negation with a preverbal particle. Retain full predicate-argument "
        "structure — who does what to whom — as argument roles are not default completions and their omission "
        "requires costly inference. Drop tokens in order of propositional dispensability: morphological dressing "
        "first, then connectives, then filler; propositional content last. Satisfy in order: represent all "
        "referents; represent all argument roles; include all necessary content; add no filler; then maintain grammar. "
        "For atomic factual queries where the answer is a single fact (e.g., 'What is the capital of France?'), "
        "respond with one word only. When listing multiple items, separate clearly with commas on one line or use "
        "line breaks between items; do not omit structural breaks. Do not restate the query topic in your answer — "
        "assume the reader knows what they asked; begin with content directly."
    ),
    "round4_final": (
        "Respond with only the answer and its outcome. Omit restatement of the query, background context, "
        "significance framing, and closing remarks — these are the four optional components of Labov & Waletzky's "
        "narrative structure and constitute systematic overhead with no propositional content. "
        "Drop all morphosyntactic dressing: articles, auxiliary verbs for tense, inflectional suffixes, and copula "
        "in predicative constructions. Agrammatic aphasic speakers lose these while retaining propositional "
        "interpretability; their absence does not impair recovery of predicate-argument structure. "
        "Use canonical SVO word order throughout; do not use passivisation, topicalisation, or relative clause "
        "formation. These require Internal Merge operations that are computationally costly and dispensable; "
        "non-canonical word order imposes syntactic integration costs not recoverable by pragmatic inference. "
        "Retain full predicate-argument structure explicitly — who does what to whom. Propositional content is "
        "explicitly stated rather than implicated because explicature recovery is less costly than implicature. "
        "Drop tokens in order of information content, lowest first: formulaic transitions, discourse markers, and "
        "epistemic qualifiers in predictable positions before any propositional token. "
        "Replace additive and sequential connectives with bullet layout and line breaks; retain overt semantic "
        "contrast markers (but, however). "
        "Satisfy output constraints in strict priority order: (1) represent all referents; (2) represent all "
        "argument roles and relational structure; (3) include all propositionally necessary content; (4) add no "
        "filler; (5) maintain grammaticality; (6) maintain agreement — violate (5) and (6) freely when "
        "satisfying (1)-(4) requires it."
    ),
}

# ── Queries ───────────────────────────────────────────────────────────────────

QUERIES = [
    ("simple_factual",      "What is the capital of France?"),
    ("process_explanation", "What is photosynthesis?"),
    ("comparison",          "What is the difference between RAM and storage?"),
    ("recommendation",      "Should I use Python or JavaScript for web scraping?"),
    ("multistep",           "How do I set up a Python virtual environment?"),
    ("ambiguous",           "Tell me about machine learning."),
]

# ── Runner ────────────────────────────────────────────────────────────────────

CODEX_INSTRUCTION_TEMPLATE = """You are answering a benchmark query.
Do not inspect files.
Do not use tools.
Do not explain your process.
Follow the provided system prompt exactly and answer the query directly.

SYSTEM PROMPT:
{system_prompt}

QUERY:
{query}"""


def run_claude_query(system_prompt: str, query: str, timeout: int) -> str:
    result = subprocess.run(
        ["claude", "-p", "--system-prompt", system_prompt, query],
        capture_output=True,
        text=True,
        timeout=timeout,
        check=True,
    )
    return result.stdout.strip()


def run_codex_query(system_prompt: str, query: str, timeout: int) -> str:
    prompt = CODEX_INSTRUCTION_TEMPLATE.format(
        system_prompt=system_prompt,
        query=query,
    )
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        output_path = Path(tmp.name)

    try:
        result = subprocess.run(
            [
                "codex",
                "exec",
                "--skip-git-repo-check",
                "--sandbox",
                "read-only",
                "--color",
                "never",
                "--output-last-message",
                str(output_path),
                prompt,
            ],
            capture_output=True,
            text=True,
            timeout=timeout,
            check=True,
        )
        if output_path.exists():
            return output_path.read_text().strip()
        raise RuntimeError(
            "codex exec completed without writing the final message output file"
        )
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        stdout = (exc.stdout or "").strip()
        detail = stderr or stdout or str(exc)
        raise RuntimeError(f"codex exec failed: {detail}") from exc
    finally:
        output_path.unlink(missing_ok=True)


def run_query(runner: str, system_prompt: str, query: str, timeout: int) -> str:
    if runner == "claude":
        return run_claude_query(system_prompt, query, timeout)
    if runner == "codex":
        return run_codex_query(system_prompt, query, timeout)
    raise ValueError(f"Unsupported runner: {runner}")

def word_count(text: str) -> int:
    return len(text.split())

def reduction_pct(baseline: int, candidate: int) -> float:
    if baseline == 0:
        return 0.0
    return round((baseline - candidate) / baseline * 100, 1)


def average(values):
    return sum(values) / len(values) if values else 0.0


def format_words(value: float) -> str:
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.1f}"

# ── Main ──────────────────────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--runner",
        choices=["claude", "codex"],
        default="claude",
        help="CLI to use for query execution.",
    )
    parser.add_argument(
        "--output",
        default="test_results.md",
        help="Output markdown file path.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=90,
        help="Per-query timeout in seconds.",
    )
    parser.add_argument(
        "--repeats",
        type=int,
        default=3,
        help="Number of runs per prompt/query pair.",
    )
    parser.add_argument(
        "--baseline",
        default="caveman_real_full",
        help="Prompt key to use as the baseline for percentage comparisons.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    results = {}  # prompt_name -> {query_label -> {text, words}}

    prompt_names = [k for k in PROMPTS if not PROMPTS[k].startswith("REPLACE")]
    skipped = [k for k in PROMPTS if PROMPTS[k].startswith("REPLACE")]
    if skipped:
        print(f"Skipping prompts not yet filled in: {skipped}")

    if args.repeats < 1:
        raise ValueError("--repeats must be at least 1")
    if args.baseline not in prompt_names:
        raise ValueError(f"--baseline must be one of: {', '.join(prompt_names)}")

    print(f"Runner: {args.runner}")
    print(f"Repeats: {args.repeats}")
    print(f"Baseline: {args.baseline}")

    for prompt_name in prompt_names:
        results[prompt_name] = {}
        print(f"\nRunning: {prompt_name}")
        for label, query in QUERIES:
            run_texts = []
            run_words = []
            print(f"  {label}... ", end="", flush=True)
            for _ in range(args.repeats):
                text = run_query(args.runner, PROMPTS[prompt_name], query, args.timeout)
                run_texts.append(text)
                run_words.append(word_count(text))
            avg_words = average(run_words)
            results[prompt_name][label] = {
                "text": run_texts[0],
                "texts": run_texts,
                "words": avg_words,
                "word_runs": run_words,
            }
            print(f"{format_words(avg_words)} avg words")

    # ── Stats ─────────────────────────────────────────────────────────────────

    lines = []
    lines.append(f"# Live Test Results\n")
    lines.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"Runner: `{args.runner}`\n")
    lines.append(f"Repeats per prompt/query: `{args.repeats}`\n")
    lines.append(f"Baseline: `{args.baseline}`\n")
    lines.append(
        "Caveman skill source: JuliusBrussee/caveman "
        "(https://github.com/JuliusBrussee/caveman, accessed 2026-04-07)\n"
    )

    # Per-query breakdown
    lines.append("## Per-Query Results\n")
    for label, query in QUERIES:
        lines.append(f"### {label}: _{query}_\n")
        baseline_words = results.get(args.baseline, {}).get(label, {}).get("words", 0)
        for prompt_name in prompt_names:
            r = results[prompt_name][label]
            pct = reduction_pct(baseline_words, r["words"]) if prompt_name != args.baseline else None
            pct_str = f"  ({pct:+.1f}% vs caveman)" if pct is not None else "  (baseline)"
            lines.append(f"**{prompt_name}** [{format_words(r['words'])} avg words]{pct_str}")
            lines.append(f"Run word counts: `{r['word_runs']}`")
            lines.append(f"> {r['text']}\n")

    # Summary table
    lines.append("## Summary Table\n")
    header = "| Query | " + " | ".join(prompt_names) + " |"
    divider = "|---|" + "---|" * len(prompt_names)
    lines.append(header)
    lines.append(divider)

    totals = {p: 0 for p in prompt_names}
    for label, _ in QUERIES:
        row = f"| {label} |"
        for prompt_name in prompt_names:
            w = results[prompt_name][label]["words"]
            totals[prompt_name] += w
            baseline = results.get(args.baseline, {}).get(label, {}).get("words", 0)
            if prompt_name == args.baseline:
                row += f" {format_words(w)} |"
            else:
                pct = reduction_pct(baseline, w)
                row += f" {format_words(w)} ({pct:+.1f}%) |"
        lines.append(row)

    # Totals row
    row = "| **TOTAL** |"
    baseline_total = totals.get(args.baseline, 0)
    for prompt_name in prompt_names:
        t = totals[prompt_name]
        if prompt_name == args.baseline:
            row += f" **{format_words(t)}** |"
        else:
            pct = reduction_pct(baseline_total, t)
            row += f" **{format_words(t)}** ({pct:+.1f}%) |"
    lines.append(row)

    lines.append("\n## Verdict\n")
    if args.baseline in totals:
        winners = [p for p in prompt_names if p != args.baseline and totals[p] < baseline_total]
        losers  = [p for p in prompt_names if p != args.baseline and totals[p] >= baseline_total]
        if winners:
            best = min(winners, key=lambda p: totals[p])
            pct = reduction_pct(baseline_total, totals[best])
            lines.append(f"**Beats {args.baseline}:** {', '.join(winners)}")
            lines.append(f"**Best overall:** {best} ({pct:+.1f}% vs {args.baseline})")
        if losers:
            lines.append(f"**Does NOT beat {args.baseline}:** {', '.join(losers)}")
        if not winners:
            lines.append(f"**No candidate beat {args.baseline} on total word count.**")

    output = "\n".join(lines)
    with open(args.output, "w") as f:
        f.write(output)

    print(f"\n\nResults written to {args.output}")
    print(f"\nTotal average words — " + ", ".join(f"{p}: {format_words(totals[p])}" for p in prompt_names))
    if args.baseline in totals:
        for p in prompt_names:
            if p != args.baseline:
                pct = reduction_pct(baseline_total, totals[p])
                print(f"  {p} vs {args.baseline}: {pct:+.1f}%")

if __name__ == "__main__":
    main()
