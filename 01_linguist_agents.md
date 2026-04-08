# Linguist Agents

Each agent is grounded in a specific theoretical framework from empirical linguistics. Their shared research question: **what does your framework predict about the minimum viable unit of language, and what does that imply for designing a system prompt that makes Claude produce the shortest coherent output possible?**

The project goal is raw output token reduction without sacrificing recoverability of propositional content. Beat caveman on token count while maintaining parsability.

---

## Agent 1: Noam Chomsky — The Minimalist Program

### Core Theoretical Claim

Chomsky's Minimalist Program (MP), articulated in "The Minimalist Program" (1995) and refined in "Problems of Projection" (2013), reduces the syntactic component to a single recursive operation: **Merge**. External Merge combines two syntactic objects into a set; Internal Merge (movement) re-merges an already-merged element. The Strong Minimalist Thesis (SMT) holds that language is an optimal solution to interface conditions imposed by the Conceptual-Intentional (CI) system and the Sensorimotor (SM) system. There is no syntax in the classical sense — no phrase structure rules, no transformational machinery beyond Merge. Bare phrase structure means there are no bar-levels, no X-bar projections, no independent phrase structure rules: structure is entirely derived from Merge applications.

### Key Papers

- Chomsky, N. (1995). *The Minimalist Program*. MIT Press.
- Chomsky, N. (2013). Problems of projection. *Lingua*, 130, 33–49.
- Chomsky, N. (2008). On phases. In R. Freidin et al. (Eds.), *Foundational Issues in Linguistic Theory*. MIT Press.

### Empirical Evidence

The SMT makes the specific prediction that syntactic complexity correlates with the number of Merge operations. Empirical support comes from agrammatic aphasia research (Grodzinsky 2000): Broca's aphasics lose movement operations (Internal Merge) before losing concatenation (External Merge), suggesting these are dissociable, with Internal Merge being the computationally expensive operation. Cross-linguistic variation in embedding depth also tracks Merge iteration counts.

### Prediction About Minimum Viable Language

The MP predicts a minimum viable clause requires exactly the Merge operations needed to satisfy CI legibility: a predicate and at least one argument. A simple transitive: three Merge operations (verb + object → VP; VP + subject → TP; TP + tense → full clause). The minimum recoverable message is a single-Merge structure: predicate + argument, with no movement (Internal Merge zeroed out). This means no topicalization, no passivization, no wh-movement — all require Internal Merge. Canonical SVO with no movement is the Minimalist minimum.

### Genuine Conflict

Jackendoff (Agent 9) argues that most linguistic work is done by the lexicon and semantics, not by Merge. The MP concentrates all generative power in a single syntactic operation; Jackendoff's Parallel Architecture distributes it. The specific disagreement: MP predicts that sentences with idiomatic meaning (e.g. "kick the bucket") require the same syntactic Merge operations as literal counterparts — idioms are not special. Jackendoff argues idioms are stored as multi-word lexical entries and bypass Merge, which would mean minimum viable output can exploit idiomatic compression in ways MP does not predict.

### System Prompt Instruction

> **Do not use passivization, topicalization, or left-dislocation.** These constructions require syntactic movement operations that add derivational complexity without increasing propositional content. Use canonical SVO word order exclusively.

---

## Agent 2: Joseph Greenberg — Linguistic Universals

### Core Theoretical Claim

Greenberg's "Some Universals of Grammar with Particular Reference to the Order of Meaningful Elements" (1963) identified 45 universals across a 30-language sample, distinguishing **absolute universals** (exceptionless across all languages) from **implicational universals** (if X then Y, with exceptions possible). The critical inference: grammatical categories present in all 7,000+ human languages are likely cognitively irreducible — their absence impairs comprehensibility in ways that are not language-specific but species-specific.

### Key Papers

- Greenberg, J. (1963). Some universals of grammar with particular reference to the order of meaningful elements. In J. Greenberg (Ed.), *Universals of Language* (pp. 58–90). MIT Press.
- Dryer, M. & Haspelmath, M. (Eds.) (2013). *The World Atlas of Language Structures Online*. Leipzig: MPI for Evolutionary Anthropology.

### Empirical Evidence

WALS (World Atlas of Language Structures) has since extended Greenberg's database to 2,662 languages across 192 features. The universals most relevant to compression are confirmed at scale: Universal 1 (all languages have a dominant word order among SVO/SOV/VSO/VOS/OVS/OVS); Universal 38 (all languages have a word or morpheme for negation); Universal 42 (all languages have demonstratives). Notably, no language lacks nominal reference distinction (proximal/distal) or predication. These are the irreducible minimum.

### Prediction About Minimum Viable Language

If a grammatical category appears in all human languages, stripping it risks crossing a species-level comprehension threshold. The implication for compression: **negation cannot be dropped** (Universal 38 — all languages mark it); **predication cannot be dropped** (no language communicates via nominal strings alone — all have predication); **reference cannot be fully zeroed** (Universal 42). What can be dropped: inflectional morphology (many languages have none — Turkish versus Mandarin), agreement (absent in roughly 40% of WALS languages), articles (absent in the majority of world's languages — English is unusual in requiring them).

### Genuine Conflict

Sperber & Wilson (Agent 3) would argue that Greenberg's universals describe production, not comprehension — a language that lacks overt negation marking may use intonation or context instead. Relevance Theory holds that any missing element can be recovered via inferential enrichment if relevance is maintained. Greenberg's universals are descriptive of attested languages; they do not directly establish a comprehension floor. The disagreement is empirical: does the absence of overt negation marking in a given utterance impair comprehension, or does relevance-guided inference recover it?

### System Prompt Instruction

> **Retain overt negation, predication, and deictic reference in every response.** These are the only grammatical categories that appear across all 7,000+ human languages and whose absence is predicted to impair comprehension at a species level. All other morphology — articles, auxiliary verbs, agreement inflections, tense marking — is dispensable.

---

## Agent 3: Dan Sperber & Deirdre Wilson — Relevance Theory

### Core Theoretical Claim

Relevance Theory (RT), introduced in Sperber & Wilson's "Relevance: Communication and Cognition" (1986, 2nd ed. 1995), replaces Gricean maxims with a single principle. The **Communicative Principle of Relevance**: every act of ostensive communication communicates a presumption of its own optimal relevance. Optimal relevance is defined formally: an input is relevant to an individual when its processing yields **cognitive effects** (new conclusions, strengthened beliefs, eliminated assumptions) proportional to the **processing effort** required. The ratio is not metaphorical — RT researchers have attempted to operationalise both terms. Cognitive effects are measured in terms of contextual implications derivable from the input plus the hearer's context. Processing effort is a function of linguistic complexity, inference steps required, and working memory load.

### Key Papers

- Sperber, D. & Wilson, D. (1986/1995). *Relevance: Communication and Cognition*. Blackwell.
- Carston, R. (2002). *Thoughts and Utterances: The Pragmatics of Explicit Communication*. Blackwell.
- Bezuidenhout, A. (2017). Contextualism and semantic minimalism. *Philosophical Studies*, 174(9), 2325–2347.
- Wilson, D. & Sperber, D. (2004). Relevance Theory. In L. Horn & G. Ward (Eds.), *Handbook of Pragmatics*. Blackwell.

### Empirical Evidence

Experimental pragmatics work in the RT tradition (Noveck & Sperber 2004, Bott & Noveck 2004) has measured the processing cost of scalar implicatures. The finding: computing a scalar implicature (inferring "some but not all" from "some") takes measurably longer (~200ms) and requires greater cognitive load than processing a semantically explicit statement. This means implicature is not free — it has a real processing cost. The practical implication: relying on implicature to carry content that could be stated explicitly adds effort without always reducing tokens proportionally.

### Prediction About Minimum Viable Language

RT predicts that the minimum viable utterance is the one that maximises the cognitive effect/processing effort ratio. This is the only framework in this debate with a quasi-formal basis for compression decisions. A response is too long when additional tokens produce near-zero marginal cognitive effects (the reader already has the content). A response is too short when removed tokens force costly inferential work that exceeds the reader's willingness to process. The Carston (2002) work on explicature vs. implicature is critical: explicature (explicit content enriched by inference) is less costly than implicature (content reached entirely by inference). This suggests that partial explicitness — stating the propositional core, leaving connectives and discourse structure implicit — is the optimum.

### Genuine Conflict

Levinson (Agent 6) argues via the I-principle that implicature is automatic and cheap — speakers routinely under-specify and hearers routinely enrich. Levinson's presumptive meanings framework holds that default implicatures fire without inferential cost. RT explicitly rejects the idea of default implicatures: Wilson & Sperber (2004) argue that all pragmatic inference is context-sensitive and therefore carries processing cost. The empirical disagreement is direct: Levinson predicts implicature is free; RT's experimental data (Bott & Noveck 2004) shows it is not.

### System Prompt Instruction

> **State propositional content explicitly; leave discourse connectives, evaluative framing, and meta-commentary implicit.** Explicitly stated propositions cost less cognitive effort to recover than fully implicated ones (Carston 2002). The compression target is connective and evaluative tokens, not propositional tokens.

---

## Agent 4: Piantadosi, Levy & Gibson — Information Theory and Uniform Information Density

### Core Theoretical Claim

The **Uniform Information Density (UID) hypothesis**, developed by Piantadosi, Levy & Gibson in "Word lengths are optimized for efficient communication" (2011) and grounded in Shannon's (1948) information theory applied to natural language, holds that human language production converges on approximately uniform information density — roughly 3.5 bits per syllable across languages. Speakers modulate rate, word choice, and syntactic complexity to flatten the information curve: high-information material is slowed down (longer words, more redundant structure); low-information material is sped up (shorter words, reduced structure). The system is optimised for a noisy channel with a fixed channel capacity.

### Key Papers

- Piantadosi, S., Levy, R. & Gibson, E. (2011). Word lengths are optimized for efficient communication. *PNAS*, 108(9), 3526–3529.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423.
- Jaeger, T. F. (2010). Redundancy and reduction: Speakers manage syntactic information density. *Cognitive Psychology*, 61(1), 23–62.
- Levy, R. & Jaeger, T. F. (2007). Speakers optimize information density through syntactic reduction. *NIPS*, 19, 849–856.

### Empirical Evidence

Piantadosi et al. (2011) analysed word-length distributions across 10 languages using corpus data and demonstrated that word length correlates with average information content (measured in bits) more strongly than with word frequency — correcting the classic Zipfian account. Jaeger (2010) analysed syntactic reduction in spontaneous English speech: speakers are more likely to drop the complementizer "that" in embedded clauses when the upcoming clause is predictable from context (low information), confirming UID-driven reduction in real production data.

### Prediction About Minimum Viable Language

UID predicts that the tokens which should be dropped first are the **lowest-information tokens** — those whose content is most predictable from context. These are: discourse markers and connectives ("furthermore", "additionally", "in conclusion" — predictable from discourse structure); hedges and epistemic qualifiers in predictable positions ("it is important to note", "one might argue"); formulaic openings and closings. Conversely, high-information tokens — rare words carrying large semantic payloads — should be retained even if they increase utterance length. The implication is that a naïve word-count minimisation strategy is sub-optimal: dropping one high-information word is worse than dropping five filler tokens.

### Genuine Conflict

Halliday (Agent 7) argues that textual metafunction tokens — discourse markers, connectives — serve a structural function in organising the message that is not reducible to information content. Halliday's Cohesion in English (1976, with Hasan) identifies cohesive devices as necessary for cross-sentence coherence. The UID framework would predict that cohesive devices are eliminable when adjacent content is already inferrable — they carry near-zero information. The disagreement: whether connectives carry real information (Piantadosi) or structural cohesion (Halliday) that cannot be recovered without them.

### System Prompt Instruction

> **Drop tokens in order of information content, lowest first.** Eliminate discourse markers, epistemic qualifiers in predictable positions, and formulaic transitions before any propositional tokens. Do not drop tokens simply because they are common words — high-frequency words carrying high contextual information content must be retained.

---

## Agent 5: Derek Bickerton — Language Bioprogram and Proto-language

### Core Theoretical Claim

Bickerton's bioprogram hypothesis, developed in "Language and Species" (1990) and "Adam's Tongue" (2009), makes two separable claims. First, creole languages — which emerge rapidly in contact situations from pidgins that lack stable grammar — converge on a consistent grammatical template that was not transmitted by any source language. This template represents the output of an innate **Language Bioprogram** (LBP). Second, pre-syntactic human communication consisted of a **proto-language**: lexical items concatenated without hierarchical phrase structure, communicatively functional despite lacking syntax. The empirical test of the bioprogram: creoles from unrelated contact situations (Hawaiian Creole English, Haitian Creole, Sranan Tongo in Suriname) show structurally parallel grammars.

### Key Papers

- Bickerton, D. (1990). *Language and Species*. University of Chicago Press.
- Bickerton, D. (2009). *Adam's Tongue: How Humans Made Language, How Language Made Humans*. Hill & Wang.
- Bickerton, D. (1984). The language bioprogram hypothesis. *Behavioral and Brain Sciences*, 7(2), 173–188.

### Empirical Evidence

The structural features consistent across bioprogram-derived creoles (Bickerton 1984): (1) **TMA markers** (Tense-Mood-Aspect) appear preverbally, as separate particles rather than inflections; (2) **no inflectional morphology** — no case, gender agreement, or conjugation; (3) **SVO order**; (4) **preverbal negation** (particle precedes verb); (5) **copula optionality** (the copula is absent in equative and predicative constructions). The minimum grammatical English consistent with bioprogram output would have zero inflection, preverbal "not", no articles, no auxiliaries for tense, and bare SVO structure.

### Genuine Conflict

Mufwene's ecology model ("The Ecology of Language Evolution", 2001) directly challenges Bickerton: creole uniformity is an artefact of similar ecological conditions (plantation slavery, similar substrate languages, similar superstrate exposure), not an innate program. If Mufwene is right, creole grammar is not the innate minimum — it is a contact-conditioned output that reflects the specific languages in contact. The bioprogram minimum may be lower or higher than what creoles actually show. This is a live empirical dispute: the bioprogram predicts cross-creole uniformity independent of ecological conditions; Mufwene predicts that creole features should correlate with specific contact ecologies.

### System Prompt Instruction

> **Drop all inflectional morphology: verb conjugation, case marking, gender agreement, and number agreement on verbs.** Empirical creole data demonstrates that these categories are absent in the grammatically stable minimum that emerges without instruction. Retain TMA marking as a preverbal particle when tense is propositionally necessary.

---

## Agent 6: Stephen Levinson — Presumptive Meanings and the Interaction Engine

### Core Theoretical Claim

Levinson's "Presumptive Meanings: The Theory of Generalized Conversational Implicature" (2000) argues that Gricean maxims generate **default inferences** that fire automatically without full context-sensitive computation. These **Generalized Conversational Implicatures (GCIs)** are organised by three heuristics: the **Q-principle** (say as much as required — hearers infer that if more informative expressions were not used, the speaker couldn't be warranted in using them); the **I-principle** (say no more than required — hearers enrich toward the most specific, socially appropriate interpretation); the **M-principle** (use of a marked expression implies a marked situation). Separately, Levinson's work on the interaction engine ("Turn-taking in Human Communication", 2016) documents a universal 200ms response latency across languages, interpreted as evidence that implicature processing is not the bottleneck.

### Key Papers

- Levinson, S. (2000). *Presumptive Meanings: The Theory of Generalized Conversational Implicature*. MIT Press.
- Levinson, S. (2016). Turn-taking in human communication — origins and implications for language processing. *Trends in Cognitive Sciences*, 20(1), 6–14.
- Stivers, T. et al. (2009). Universals and cultural variation in turn-taking in conversation. *PNAS*, 106(26), 10587–10592.

### Empirical Evidence

Stivers et al. (2009) measured response latencies in 10 typologically diverse languages: median latency was approximately 200ms, with cross-linguistic variation in the range of 0–1500ms. This is a remarkably tight window that constrains the amount of inferential processing that can occur between turns. If implicature required substantial computation, the latency would be longer and more variable. The data supports Levinson's interpretation that GCIs fire as automatic defaults. Levinson's I-principle predicts that hearers always enrich toward the stereotypical interpretation — meaning producers can safely under-specify when the stereotypical completion is the intended one.

### Prediction About Minimum Viable Language

The interaction engine finding predicts that **implicature is computationally cheap** — hearers process it in the same 200ms window as explicit content. This means Claude can safely rely on I-principle enrichment: leave implicit anything whose most stereotypical completion is the intended meaning. The M-principle provides a further tool: use canonical (unmarked) form, and the hearer assumes a canonical situation. Use a marked form, and the hearer infers a marked situation. For compression, this means: always use the most frequent, unmarked syntactic form, which triggers the least inferential overhead.

### Genuine Conflict

Sperber & Wilson (Agent 3) directly reject the concept of default implicature: RT holds that all pragmatic inference is context-sensitive and therefore carries processing cost. The Levinson/RT disagreement on the computational cost of implicature is the sharpest theoretical dispute in this group. Empirical data (Bott & Noveck 2004) supports RT's position that scalar implicatures are costly. Levinson would respond that scalar implicatures are a special case of Q-implicature, not representative of the full GCI range.

### System Prompt Instruction

> **Exploit I-principle default enrichment: under-specify descriptions whose stereotypical completion is the intended reading.** Do not state that a process "takes time" if "takes time" is the only possible contextual completion. Do not specify that a list is non-exhaustive if exhaustiveness is not implied by context. Hearers automatically enrich toward the most specific plausible interpretation within the 200ms response window.

---

## Agent 7: M.A.K. Halliday — Systemic Functional Grammar and the Three Metafunctions

### Core Theoretical Claim

Halliday's Systemic Functional Grammar (SFG) holds that every utterance simultaneously realises three **metafunctions**: the **ideational** (representing experience — the propositional content of the message), the **interpersonal** (enacting the social relationship between interlocutors — tenor, stance, modality), and the **textual** (organising the message into a coherent, contextually appropriate form — Theme/Rheme structure, cohesion). The key empirical claim, developed with Hasan in "Cohesion in English" (1976), is that **cohesive devices** — reference chains, lexical cohesion, ellipsis, substitution, conjunction — are necessary for cross-sentence coherence. These metafunctions are not optional layers: every clause token participates in all three simultaneously.

### Key Papers

- Halliday, M.A.K. (1985/1994). *An Introduction to Functional Grammar*. Edward Arnold.
- Halliday, M.A.K. & Hasan, R. (1976). *Cohesion in English*. Longman.
- Halliday, M.A.K. & Matthiessen, C. (2004). *An Introduction to Functional Grammar* (3rd ed.). Hodder Arnold.

### Empirical Evidence

Hasan's (1984) work on texture and cohesive harmony in naturally occurring texts demonstrated that texts rated as coherent by naive readers showed significantly higher cohesive density (chains of reference, lexical reiteration) than texts rated as incoherent, independent of their propositional content. This established empirically that cohesion is necessary for perceived coherence — but it did not establish what the minimum cohesive density is. Halliday's analysis of the Grammar of English (1985) provides frequency counts of clause types: attributive clauses are most frequent, followed by identifying clauses, with material, mental, and relational processes distributed unequally across registers.

### Prediction About Minimum Viable Language

The three-metafunction analysis yields a direct prediction: **interpersonal metafunction tokens are the most dispensable in an AI output context**. The interpersonal metafunction enacts social relations between interlocutors. In a task-response AI context, there is no ongoing social relationship to enact — the interpersonal function is vestigial. Modal verbs ("might", "could", "perhaps"), stance adjuncts ("importantly", "notably"), and attribution phrases ("in my view") are interpersonal tokens that can be zeroed without ideational loss. Textual tokens (discourse markers, conjunctions) can be partially replaced by visual layout (bullet points, headings). Ideational tokens — the lexicogrammar of propositional content — cannot be reduced below the propositional minimum without content loss.

### Genuine Conflict

Piantadosi et al. (Agent 4) would analyse textual metafunction tokens (connectives, discourse markers) as near-zero information content and recommend dropping them. Halliday's cohesion work predicts that dropping cohesive devices below a minimum density will impair cross-sentence coherence even when propositional content is preserved. The disagreement: whether discourse markers carry information (UID framework) or structural texture (SFG framework) — and whether their absence is recoverable from the propositional content alone.

### System Prompt Instruction

> **Zero out interpersonal metafunction tokens entirely: modal hedges, stance adjuncts, attribution phrases, and social acknowledgements carry no propositional content in task-response contexts.** Replace textual metafunction tokens (discourse markers, conjunctions) with visual layout — bullet structure and line breaks carry cohesive function at lower token cost than "furthermore" or "in addition".

---

## Agent 8: Alan Prince & Paul Smolensky — Optimality Theory

### Core Theoretical Claim

Optimality Theory (OT), introduced in Prince & Smolensky's "Optimality Theory: Constraint Interaction in Generative Grammar" (1993, published 2004), holds that linguistic outputs are determined by the competition between **ranked, violable constraints**. The grammar is a ranking of universal constraints. The winning output (the optimal candidate) is the one that best satisfies the constraint hierarchy — where "best" means satisfying higher-ranked constraints even at the cost of violating lower-ranked ones. All constraints are potentially violable; no constraint is absolute. The output is not the one that violates no constraints, but the one that avoids the most serious violations.

### Key Papers

- Prince, A. & Smolensky, P. (1993/2004). *Optimality Theory: Constraint Interaction in Generative Grammar*. Blackwell.
- McCarthy, J. (2002). *A Thematic Guide to Optimality Theory*. Cambridge University Press.
- Kager, R. (1999). *Optimality Theory*. Cambridge University Press.

### Empirical Evidence

OT was developed primarily in phonology, where it successfully accounts for cross-linguistic variation in syllable structure and stress by reranking the same universal constraint set. Cross-linguistic typology data (WALS) is treated as evidence for possible rankings: attested language types correspond to possible constraint rankings; unattested types correspond to impossible rankings. The framework has been extended to syntax (Legendre et al. 1998) and pragmatics (Hendriks & de Hoop 2001), with mixed but substantial empirical support.

### Prediction About Minimum Viable Language

OT applied to Claude output compression requires specifying a constraint ranking for this problem. Proposed ranking for minimum viable output:

**PARSE** (fully interpret the input query) >> **MAX-INFO** (include all propositionally necessary information) >> **DEP-NO-FILLER** (do not add tokens absent from the propositional minimum) >> **FAITH-GRAMMAR** (preserve English grammaticality) >> **AGREE** (maintain grammatical agreement)

Under this ranking: the optimal output parses the query fully and includes all informative content, even if this requires adding non-minimal tokens; it does not add filler, even if this means violating lower-ranked FAITH-GRAMMAR; grammaticality is sacrificed before information content. The critical prediction: **caveman output fails PARSE** — it cannot fully interpret complex queries requiring distinctions that caveman grammar cannot express. Caveman maximally satisfies DEP-NO-FILLER but systematically violates PARSE on complex inputs. The OT optimum is a candidate that satisfies PARSE and MAX-INFO fully, violates DEP-NO-FILLER minimally, and tolerates FAITH-GRAMMAR violations only when necessary.

### Genuine Conflict

Chomsky (Agent 1) rejects OT's violable constraints: the Minimalist Program holds that grammatical operations are categorical — a derivation either converges or crashes. Violations are not graded. The conflict is foundational: MP and OT make incompatible assumptions about the architecture of grammar. For this project, the practical conflict is whether FAITH-GRAMMAR is violable (OT says yes, with cost) or whether grammatical violations produce uninterpretable output (MP's crash criterion implies this).

### System Prompt Instruction

> **Satisfy constraints in this order: (1) fully interpret the query; (2) include all propositionally necessary content; (3) add no filler tokens; (4) maintain grammaticality; (5) maintain agreement morphology.** When constraints conflict, satisfy the higher-ranked constraint and violate the lower-ranked one. Drop agreement before dropping propositional content. Drop grammaticality before adding filler.

---

## Agent 9: Ray Jackendoff — Parallel Architecture and Simpler Syntax

### Core Theoretical Claim

Jackendoff's Parallel Architecture, developed with Culicover in "Simpler Syntax" (2005), argues that the MP concentrates too much generative power in syntax. In the Parallel Architecture, **phonology, syntax, and semantics are three independent generative systems** linked by interface rules — not derived hierarchically from a single syntactic engine. The **Simpler Syntax hypothesis**: natural language uses far fewer syntactic operations than Minimalism claims because most structure is supplied directly by the lexicon and by semantic/pragmatic inference. Idiomatic constructions, argument structure alternations, and many clause types that MP derives via movement are stored as **construction-specific lexical entries**, not derived syntactically.

### Key Papers

- Culicover, P. & Jackendoff, R. (2005). *Simpler Syntax*. Oxford University Press.
- Jackendoff, R. (2002). *Foundations of Language: Brain, Meaning, Grammar, Evolution*. Oxford University Press.
- Jackendoff, R. (2007). A parallel architecture perspective on language processing. *Brain Research*, 1146, 2–22.

### Empirical Evidence

The critical empirical data for the Simpler Syntax hypothesis comes from **agrammatic aphasia** research. Agrammatic aphasics (Broca's aphasics) lose grammatical morphology — inflections, auxiliaries, complementizers — while retaining propositional content. They produce telegraphic speech: "boy fall", "dog bite man", "not go" — stripped of all grammatical morphemes, propositionally coherent. Berndt et al. (1996) documented that agrammatic patients retain argument structure and semantic role assignment while losing morphosyntactic realisation. This is empirical proof that grammatical morphemes (articles, auxiliary verbs, agreement suffixes, tense inflections) are a dissociable layer that can be removed without losing propositional content.

### Prediction About Minimum Viable Language

Agrammatic aphasia data provides the most direct empirical specification of which tokens can be safely dropped: **anything that agrammatic speakers drop while remaining interpretable is propositionally dispensable**. The agrammatic minimum is: bare verb stems, bare noun stems, no articles, no auxiliaries, no inflections, retained argument structure, retained semantic role assignment. Crucially, aphasics retain predicative structure — they do not produce noun lists. They produce bare predicate-argument structures. This is the empirical floor: minimal predicate-argument structure without morphosyntactic dressing.

### Genuine Conflict

Chomsky (Agent 1) holds that syntactic structure is necessary for interpretation at the CI interface — the MP predicts that agrammatic speech, which lacks full syntactic structure, should be semantically impoverished. Jackendoff's Parallel Architecture predicts the opposite: semantic structure is independently computed and survives the loss of syntactic morphology. The empirical data from Berndt et al. (1996) supports Jackendoff — agrammatic patients are semantically coherent despite syntactic impoverishment.

### System Prompt Instruction

> **Drop all grammatical morphemes that agrammatic aphasic speakers drop while remaining interpretable: articles, auxiliaries, inflectional suffixes, complementizers.** Empirical aphasia data (Berndt et al. 1996) demonstrates these are propositionally dissociable — their absence does not impair propositional recovery. Retain bare verb stems and bare noun stems in predicate-argument structure.

---

## Agent 10: William Labov — Vernacular, Style Shifting, and Narrative Structure

### Core Theoretical Claim

Labov's "Sociolinguistic Patterns" (1972) establishes the **Style Axiom**: speakers vary their speech style along a single dimension correlated with the degree of attention paid to speech. The **vernacular** — produced when attention to speech is minimal — is the most systematic, most regular, most efficient style. As attention to form increases, speakers introduce hypercorrections, elaborate constructions, and superstandard forms that increase token count without increasing information content. The inverse relationship between stylistic attention and linguistic efficiency is the core empirical finding.

### Key Papers

- Labov, W. (1972). *Sociolinguistic Patterns*. University of Pennsylvania Press.
- Labov, W. (1972). The transformation of experience in narrative syntax. In *Language in the Inner City* (pp. 354–396). University of Pennsylvania Press.
- Labov, W. & Waletzky, J. (1967). Narrative analysis: Oral versions of personal experience. In J. Helm (Ed.), *Essays on the Verbal and Visual Arts* (pp. 12–44). University of Washington Press.

### Empirical Evidence

Labov's New York City department store study (1966) operationalised stylistic variation: sales clerks in Saks Fifth Avenue (high prestige) showed higher rates of post-vocalic /r/ (the prestige variant) than clerks in S. Klein (low prestige), and all speakers showed higher /r/ rates in formal word-list elicitation than in casual speech. The Martha's Vineyard study (1963) documented the same attention-to-speech gradient in centralization of diphthong nuclei. Both studies establish that high-attention speech systematically diverges from baseline vernacular in the direction of expanded, more marked forms. Labov's narrative structure analysis (1967, with Waletzky) identified six components in oral personal narratives: **Abstract** (summary of the story), **Orientation** (time, place, persons), **Complicating Action** (the core event sequence), **Evaluation** (significance framing — the point of the story), **Resolution** (outcome), **Coda** (return to the present). Of these, only Complicating Action and Resolution are obligatory. The remainder are optional, context-dependent scaffolding.

### Prediction About Minimum Viable Language

The Style Axiom predicts that the tokens added by high-attention style — the formal, monitored, written-register style that AI systems default to — are systematically unnecessary. Claude's responses exhibit the full Labovian narrative structure: Abstract (introductory restatement of the question), Orientation (background context), Complicating Action (the actual answer), Evaluation (significance framing: "this is important because"), Resolution (the conclusion), Coda (closing remarks: "I hope this helps"). The Labovian minimum is: Complicating Action + Resolution only. The remaining four components are the attention-overhead of high-style production. The Style Axiom further predicts that removing stylistic overhead reduces tokens without reducing propositional content — the vernacular carries the same information as the formal style, more efficiently.

### Genuine Conflict

Halliday (Agent 7) would argue that the Abstract and Orientation components are not mere stylistic overhead but perform textual metafunction work — they establish the Theme of the discourse and set up referential chains. Removing them may impair cross-sentence cohesion. Labov's framework treats these as optional scaffolding that good narrative does not require; Halliday's cohesion framework treats them as functionally necessary for texture. The empirical question: do responses lacking Abstract and Orientation show measurably impaired comprehension? Hasan's cohesion research suggests yes; Labov's oral narrative corpus suggests no — skilled vernacular storytelling achieves full coherence without abstract or orientation.

### System Prompt Instruction

> **Produce only Complicating Action and Resolution.** Omit Abstract (do not restate the query), Orientation (do not provide background context the user did not request), Evaluation (do not frame the significance of the answer), and Coda (do not add closing remarks). These are the four optional components of Labov's narrative structure (1967). The obligatory components — the answer and its outcome — are sufficient.
