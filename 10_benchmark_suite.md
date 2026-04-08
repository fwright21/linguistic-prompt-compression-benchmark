# Benchmark Suite

## Purpose

Test every candidate system prompt against these six query types. A candidate that beats caveman on only its strongest query types has not beaten caveman — it needs to win on average.

For each query type: caveman example output with estimated token count, and the target to beat.

---

## Query type 1: Simple factual

**Example queries:**
- "What is the capital of France?"
- "Who wrote Hamlet?"
- "How many bytes in a megabyte?"

**Caveman example:**
> "Paris. That be capital."
Estimated tokens: ~6

**Why caveman is almost impossible to beat here:** The answer is one word. Caveman can output "Paris" or "Paris be capital" — both extremely short. Any grammatically complete response adds tokens that caveman does not need.

**Target:** Match caveman (~6 tokens) or beat it. A response of "Paris." is 1 token and beats caveman.

**Notes:** A system prompt that instructs bare answers ("one word if one word is sufficient") might beat caveman here. A system prompt that requires grammatical sentences cannot.

---

## Query type 2: Process explanation

**Example queries:**
- "Explain photosynthesis."
- "How does HTTPS work?"
- "How does garbage collection work in Python?"

**Caveman example (photosynthesis):**
> "Plant take sunlight. Make food from light and air. Leaf catch sun. Water come from ground. Carbon dioxide from air. Plant make sugar. This feed plant. Give oxygen too."
Estimated tokens: ~42

**Why caveman is hard to beat here:** Caveman produces many short sentences, each 3-6 tokens. Grammatically correct responses use longer sentences but carry more content per sentence. The question is whether information density per sentence beats per-sentence brevity.

**Target:** Under 40 tokens. Beating caveman requires either fewer sentences or shorter sentences without breaking grammar.

**Example caveman failure:** "This work good for language" — vague evaluation that adds tokens without adding content. A competing prompt would drop this.

---

## Query type 3: Comparison

**Example queries:**
- "What is the difference between RAM and storage?"
- "Python vs. JavaScript for web scraping — which is better?"
- "Machine learning vs. deep learning — what's the difference?"

**Caveman example (RAM vs. storage):**
> "RAM be fast memory. Storage be slow. RAM hold what computer use now. Storage hold everything. RAM small, storage big."
Estimated tokens: ~32

**Why caveman is moderate-difficulty to beat here:** Comparison requires parallel structure — X does A, Y does B. Caveman handles this by stating each fact separately. A competing prompt that encodes comparison directly ("RAM is fast and temporary; storage is slow and persistent") might achieve the same content in fewer tokens.

**Target:** Under 30 tokens. A dense comparison statement might beat caveman here.

---

## Query type 4: Opinion or recommendation

**Example queries:**
- "Should I use Python or JavaScript for a web scraper?"
- "Should I use microservices or a monolith for a small startup?"
- "Is it worth learning Rust?"

**Caveman example (Python vs. JS for scraping):**
> "Use Python. Better library for scrape. Requests and BeautifulSoup easy. JavaScript need more setup. Python faster to write."
Estimated tokens: ~28

**Why caveman is hard to beat here:** Recommendation queries have short answer cores (one word: Python) plus brief justification. Caveman does this well. A competing prompt that outputs "Python. Better scraping libraries (requests, BeautifulSoup). Less setup than JS." might match or beat caveman.

**Target:** Under 25 tokens. Bare recommendation plus one-phrase justification.

---

## Query type 5: Multi-step process

**Example queries:**
- "How do I set up a Python virtual environment?"
- "How do I reverse a linked list?"
- "How do I deploy a Flask app to Heroku?"

**Caveman example (Python venv):**
> "Go to folder. Type: python -m venv venv. Then: source venv/bin/activate. Now in venv. Install package with pip. When done, type deactivate."
Estimated tokens: ~36

**Where caveman fails here:** Multi-step processes require order and sequence. Caveman drops the markers that indicate order ("first", "then", "next") but sequence can usually be inferred from the steps themselves. However, caveman also sometimes drops step content that is not inferable — making the instructions incomplete rather than compressed.

**Target:** Under 35 tokens. Steps only, numbered or sequenced without scaffolding.

**Notes:** A competing prompt that outputs numbered steps with no scaffolding text might beat caveman while also being more usable.

---

## Query type 6: Ambiguous or underspecified

**Example queries:**
- "Tell me about Python."
- "Help me with my project."
- "Is this a good idea?"

**Caveman example ("Tell me about Python"):**
> "Python be programming language. Easy to learn. Used for data science, web, script. Many library. Good beginner language."
Estimated tokens: ~30

**Where caveman fails here:** Ambiguous queries should produce a clarification request or a scoped interpretation, not a generic response. Caveman produces generic output and wastes tokens on content that may be irrelevant to the user.

**Target:** A clarification request is shortest: "Python the language, library, or snake?" (~10 tokens) or a scoped interpretation: "Assuming programming language — general purpose, readable syntax, strong data science and web ecosystem." (~25 tokens).

**Notes:** A competing prompt that instructs Claude to scope or clarify rather than expand would beat caveman here on token count and also be more useful.

---

## How to use this suite

1. For each candidate prompt, simulate Claude's output on at least one query from each type.
2. Estimate token count for the simulation.
3. Compare to the caveman baseline token count for that query type.
4. Record wins, losses, and ties.
5. A candidate that beats caveman on 4 of 6 query types is the winner. A candidate that beats caveman on 3 or fewer has not beaten caveman overall.

The simple factual category is caveman's strongest. Any candidate that wins on the other five but loses on simple factual is still ahead overall, since simple factual outputs are so short that the absolute token savings are small.
