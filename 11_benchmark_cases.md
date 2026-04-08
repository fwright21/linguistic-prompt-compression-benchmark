# Round Three Debate — Empirical Benchmarks: Minimal Language in the Wild

**Agents:** Levinson (Presumptive Meanings/Interaction Engine), Bickerton (Bioprogram/Proto-language), with Greenberg (returning as judge on Bickerton vs. Mufwene) and OT (returning as judge on constraint ranking)
**Core question:** What does the empirical record of minimal languages — pidgins, creoles, agrammatic aphasia, child language, proto-language hypotheses — tell us about the irreducible minimum? What do these cases imply for a system prompt constraining Claude output?
**Benchmark query used in examples:** "What is the difference between RAM and storage?"

**Caveman baseline response:**
> "RAM be fast memory. Storage be slow. RAM hold what computer use now. Storage hold everything. RAM small, storage big."

Estimated tokens: ~32

---

## Part 1 — Opening Statements

### Bickerton — Language Bioprogram and Proto-language

The empirical record of creole formation provides the most direct available evidence about what grammatical minimum emerges when untrained speakers build a language from scratch under communicative pressure. The bioprogram hypothesis (Bickerton 1984; "Language and Species" 1990) makes a strong empirical claim: creole languages that emerge from pidgins in unrelated contact situations converge on a consistent grammatical template not transmitted by any source language. This template is the output of the Language Bioprogram — an innate specification of grammatical structure that is recruited when the input is too degraded to acquire from ambient language.

The structural features consistent across bioprogram-derived creoles — Hawaiian Creole English, Haitian Creole, Sranan Tongo (Suriname), Tok Pisin (Papua New Guinea), Mauritian Creole — are (Bickerton 1984): **(1) TMA markers** appear preverbally as separate particles rather than inflectional suffixes (Haitian Creole: *te* for past, *pral* for future, *ap* for progressive; Sranan: *ben* for past, *sa* for future, *e* for progressive); **(2) no inflectional morphology** — no case marking, no gender agreement, no verb conjugation for person or number; **(3) SVO word order** throughout; **(4) preverbal negation** — the negative particle precedes the verb; **(5) copula optionality** — the copula is absent in equative and predicative constructions ("she doctor" rather than "she is a doctor").

These five features are the bioprogram minimum. They represent what emerges when the grammar-building capacity operates without instruction. The inference for Claude output compression is direct: a grammar that matches bioprogram output is not broken English — it is the minimum grammatical English consistent with the innate language faculty. It is more grammatically stable than caveman (which deviates from SVO, lacks TMA marking, and has no systematic structure) and more compressed than standard English.

For the RAM/storage query, the bioprogram minimum produces: "RAM fast. Storage slow. RAM hold current data. Storage hold all data. RAM smaller." No copula (optionality), no articles (absent in bioprogram), no inflection on "hold" for agreement, TMA marking unnecessary because the description is generic-present. This is approximately 18 tokens — significantly under the caveman baseline of 32.

**Predicted minimum:** Bioprogram grammar — SVO, no inflection, no articles, no copula in predicative constructions, preverbal negation particle, TMA particles only when tense is propositionally necessary.

---

### Levinson — Presumptive Meanings and the Interaction Engine

The empirical record of minimal language does not speak with a single voice, and the bioprogram hypothesis attributes to innateness a set of features that may be better explained by the constraints of interaction itself. My contribution to this round draws on two empirical programmes: the Generalized Conversational Implicature framework ("Presumptive Meanings" 2000) and the interaction engine research programme (Levinson 2016; Stivers et al. 2009).

The **interaction engine** finding is the more fundamental for this debate. Stivers et al. (2009) measured response latencies in 10 typologically diverse languages — English, Danish, Dutch, Yélî Dnye (Papua New Guinea), Lao, Japanese, Tzeltal (Mexico), Akhoe Hai||om (Namibia), Italian, and Korean. The median response latency across all languages was approximately 200ms, with cross-linguistic variation in the range of 0–1500ms. This 200ms window is the time available for a speaker to plan and initiate a response while the current speaker is still speaking — it requires that the hearer be predicting the end of the current turn in real time. This constraint shapes what can be compressed in spoken language: anything that requires more than 200ms of inferential computation cannot be safely omitted from a turn, because the response window closes before the inference completes.

The implication for compression is the **opposite of what RT predicts** from the Bott & Noveck (2004) data. Levinson's I-principle holds that Generalized Conversational Implicatures (GCIs) — default inferences generated by the I-heuristic "say no more than required; hearers enrich toward the most specific plausible interpretation" — fire automatically within the 200ms window. They are not computed by effortful pragmatic reasoning; they are default completions that activate as automatically as lexical access. Levinson (2000) argues that GCIs are pre-computed defaults that apply unless cancelled — the burden of processing is on cancellation, not on enrichment.

This means that under-specification is reliable and cheap when the most stereotypical completion is the intended meaning. "RAM fast, storage slow" — produced without copula, without articles, in the context of a question about RAM vs. storage — will be enriched by the hearer's I-principle to "RAM is fast, storage is slow" automatically, within the 200ms response window, without effortful computation. The enrichment is a default completion, not a pragmatic inference requiring attention and working memory.

The **Q-principle** provides a complementary tool: if a speaker does not use a more informative expression that they could have used, the hearer infers they are not warranted in it. This means that Claude's use of the unmarked, less informative form — "RAM fast" rather than "RAM is very fast" — communicates by Q-implicature that Claude is not warranted in a stronger claim. This is informative about Claude's epistemic state, at no additional token cost.

**Predicted minimum:** Exploit I-principle default enrichment: under-specify descriptions whose stereotypical completion is the intended reading; rely on the 200ms automatic completion window to supply copulas, articles, and other grammatical morphemes that are predictable default completions; use Q-implicature to communicate the limits of warranted inference without epistemic hedging tokens.

---

### Greenberg — Returning Judge on Bickerton vs. Mufwene

As the agent with the most direct stake in the cross-linguistic universals question, I am positioned to evaluate the central empirical dispute of this round: whether Bickerton's bioprogram predicts genuine cross-creole uniformity, or whether Mufwene's ecology model ("The Ecology of Language Evolution" 2001) explains the same data without the innateness hypothesis.

Mufwene argues that creole uniformity is not evidence of an innate bioprogram but of **similar ecological conditions**: plantation creoles arose in similar sociolinguistic environments — large numbers of speakers of related substrate languages (West African languages with similar typological profiles), a single dominant superstrate (English, French, or Portuguese), and the same social conditions of restricted access to the superstrate (Mufwene 2001, chapters 1–3). On Mufwene's account, if you hold ecological conditions constant, you predict similar output — not because of innateness, but because similar inputs produce similar outputs through the same contact processes. The test: creoles arising from ecologically different contact situations should show different grammatical profiles. Mufwene argues that the data supports this: trade contact languages (with access to the superstrate) look different from plantation creoles (with restricted superstrate access).

From a Greenbergian universals perspective, the Bickerton-Mufwene dispute matters enormously for the compression project. If Bickerton is right, the bioprogram minimum is a specification of innate grammatical universals — it is as robustly attested as any WALS universal, and arguably more theoretically grounded (it is derived, not merely described). If Mufwene is right, the bioprogram minimum is an ecological artefact — it reflects the specific substrates and superstrates of Atlantic plantation creoles, not a universal grammatical minimum.

The universals evidence is partially consistent with both accounts. WALS confirms that SVO order is the most common word order type globally (Universal 1, confirmed in all attested creoles). WALS confirms that preverbal negation is attested in a significant proportion of SOV and SVO languages. However, WALS also documents substantial cross-creole variation that the strict bioprogram account has difficulty accommodating: Saramaccan (a Surinamese creole with Portuguese and English input) has SOV order in some VP configurations; Palenquero (a Colombian Afro-Hispanic creole) has postverbal tense marking — a direct violation of Bickerton's bioprogram feature (1).

**Judge's verdict on Bickerton vs. Mufwene:** The evidence supports a middle position. The core bioprogram features — SVO, no inflection, copula optionality — are robust enough across creoles that some innate preference is plausible, consistent with the universals data. However, TMA preverbal particle placement is not absolute — Saramaccan and Palenquero are genuine counterexamples. The compression implication: treat SVO, no inflection, no articles, and copula optionality as robustly supported by both universals data and creole data; do not rely on preverbal TMA particle placement as a categorical rule, since it is ecologically conditioned rather than universally innate.

---

### Optimality Theory — Returning Judge on Constraint Ranking

My role in this round is to evaluate the constraint ranking proposed in Round 2 against the empirical cases introduced by Bickerton and Levinson, and to determine whether the ranking requires revision in light of the proto-language and interaction engine evidence.

The Round 2 ranking was: PARSE >> MAX-INFO >> DEP-NO-FILLER >> FAITH-GRAMMAR >> AGREE.

The proto-language evidence from Bickerton introduces a new empirical case that stress-tests FAITH-GRAMMAR. Bickerton's proto-language — pre-syntactic lexical concatenation — is the limit case: pure content words, no grammatical structure at all, no FAITH-GRAMMAR, no AGREE. "Mammoth — river — east — tomorrow" (a hypothetical proto-language utterance meaning "there is a mammoth at the eastern river tomorrow" — Bickerton 2009). This violates FAITH-GRAMMAR and AGREE completely, but satisfies PARSE (all propositional content is present — referents identified, relation inferrable from world knowledge and context) and MAX-INFO. Under the Round 2 ranking, this is the optimal candidate: PARSE and MAX-INFO are satisfied; DEP-NO-FILLER is satisfied; only FAITH-GRAMMAR and AGREE are violated, and they rank below the satisfied constraints.

But proto-language output fails for Claude in a way it does not fail for early hominids: the PARSE constraint for Claude includes the requirement to represent **argument structure** — who did what to whom — not merely to list referents. "Mammoth — river — east — tomorrow" fails PARSE for a query requiring relational information (not just referential information), because the argument roles are not represented. A more precise formulation of PARSE splits it: **PARSE-REF** (represent all referents) >> **PARSE-ARG** (represent argument roles and relational structure). Proto-language satisfies PARSE-REF but violates PARSE-ARG. For simple comparison queries (RAM vs. storage), PARSE-ARG requires that the contrastive relation be represented, not merely that the two terms appear.

The interaction engine evidence from Levinson introduces a timing constraint not captured in the Round 2 ranking: inferential recovery must be completable within the 200ms response window. This does not change the constraint ranking but does affect which violations of FAITH-GRAMMAR and AGREE are acceptable: violations that require multi-step pragmatic inference to recover are more costly than violations that trigger automatic I-principle enrichment. A missing copula ("RAM fast") triggers automatic default completion within 200ms; a missing subject argument may require more costly inference about what the subject is.

**OT judge's revised ranking:** PARSE-REF >> PARSE-ARG >> MAX-INFO >> DEP-NO-FILLER >> FAITH-GRAMMAR >> AGREE, with the additional stipulation that FAITH-GRAMMAR violations are acceptable only when the missing element is recoverable within the 200ms I-principle window (Levinson 2000).

---

## Part 2 — Cross-Examination

### Clash 1: Bickerton vs. Levinson
**Bickerton's bioprogram says creole universals are innate — SVO, TMA preverbal, preverbal negation, no inflection. Levinson's interaction engine says turn-taking constraints (200ms latency) shape what gets compressed more than innateness. These are competing accounts of WHY minimal language has the features it has.**

**Bickerton:** The interaction engine cannot explain the specific grammatical features of creole output. Turn-taking pressure affects timing — it explains why speakers need to be ready to respond quickly, and why utterances need to be short enough to plan in real time. But it does not explain why creoles universally place TMA markers preverbally rather than postverbally, or why they prefer SVO over SOV or VSO. If interaction pressure were the explanation for creole grammar, we would expect creole features to track the features of the easiest-to-plan structures under time pressure — which might be SOV (verb-final, easiest for production because the verb can be planned last after the arguments are committed) or bare noun-verb sequences. Creoles don't show this: they show SVO with preverbal TMA, which is not obviously the production-easiest order.

**Levinson:** The 200ms window constrains not just when the response starts but what format allows the fastest production and comprehension in the iterative context of conversation. SVO is the production-easiest order in a **comprehension-optimised** communication system: hearers in SVO languages show faster online parsing of canonical order (Hawkins 2004, on performance-grammar correspondence). Preverbal placement of TMA markers is optimal for the interaction engine because it provides the grammatical frame information earliest — the hearer knows tense and modality before the predicate arrives, which supports predictive parsing and the 200ms response-initiation window. Preverbal negation similarly flags the negative polarity before the verb arrives, which allows the hearer to begin constructing the negative proposition earlier. The interaction engine predicts these features on processing grounds, without recourse to innateness.

**Bickerton's reply:** The processing account is plausible for SVO and preverbal TMA separately, but it does not explain their **co-occurrence** in creoles from typologically unrelated contact situations — including situations where the substrate and superstrate languages have different orders. Haitian Creole has preverbal TMA despite French (its superstrate) having postverbal tense inflection and Fon (a major substrate language) having SOV order with postverbal TAM. The emergence of SVO + preverbal TMA in Haitian Creole cannot be attributed to either processing optimality (which would predict different features from different starting orders) or substrate/superstrate transmission (which would predict French postverbal tense or Fon SOV). The bioprogram is the best explanation for the specific pattern of co-occurrence.

**Levinson's concession and counter-concession:** Bickerton's Haitian Creole case is the strongest evidence for the bioprogram — the specific features are not predictable from substrate or superstrate alone. I accept that innateness may contribute. My counter-concession: the interaction engine provides an independent functional explanation for why those specific features are optimal, which means the bioprogram may be innate because it encodes processing-optimal structures, not as a distinct innate grammatical specification. The evolutionary story and the processing story are compatible: innateness may have evolved because interaction-optimal structures are adaptive.

**Resolution of Clash 1:** Bickerton's strongest case — the Haitian Creole evidence — is not explained by processing optimality alone. Levinson's strongest case — that preverbal TMA and SVO are processing-optimal — is compatible with but does not require the bioprogram. The compression implication survives regardless of which account is correct: SVO, preverbal negation, no inflection, and copula optionality are both innate-preferred (Bickerton) and processing-optimal (Levinson). Both accounts support their retention in minimal output. The mechanism dispute does not affect the compression recommendation.

---

### Clash 2: Bickerton vs. Mufwene (introduced as counterpoint)
**Mufwene's ecology model says creoles are NOT uniform — contact conditions determine outcomes, not bioprogram. If Mufwene is right, there is no universal creole minimum to borrow from.**

**Bickerton:** Mufwene's ecological account predicts that creole features should track the specific contact ecology — the substrate languages, the superstrate, the degree of access to the superstrate, the ratio of L1 to L2 speakers in the contact pool. If this is correct, creoles from ecologically similar contact situations should be similar, and creoles from ecologically different situations should diverge. The empirical test: compare Atlantic plantation creoles (similar ecology: West African substrates, European superstrates, low superstrate access) with Pacific plantation creoles (different substrates: Melanesian, Polynesian, Austronesian; same superstrate: English or German; different conditions). If Mufwene is right, Pacific creoles should diverge significantly from Atlantic creoles. They do not: Tok Pisin, Bislama, and Solomon Islands Pijin share SVO, no inflection, copula optionality, and preverbal negation with Atlantic creoles — despite utterly different substrate languages. This cross-ocean convergence is not predicted by Mufwene's ecology model; it is predicted by the bioprogram.

**Mufwene (via Greenberg as judge):** Mufwene's response to this argument (2001, chapter 4) is that Pacific and Atlantic creoles share a European superstrate, which accounts for the surface similarities. English has SVO; English has no inflection reduction (relative to the substrates); English has copula presence in contexts where creoles show optionality. The European superstrate is the common factor, not an innate bioprogram. The features Bickerton attributes to the bioprogram are those features of the European superstrate that survived simplification under acquisition pressure — they survived not because they are innate but because they are less marked (simpler to learn) than the superstrate alternatives.

**Greenberg's verdict:** The Mufwene account has genuine force for Atlantic and Pacific creoles that share a European superstrate. The decisive test is creoles from non-European superstrates. Arabic-based creoles (Ki-Nubi in Uganda; Juba Arabic in South Sudan) show SVO order despite Arabic being a VSO language, and they show copula optionality despite Arabic having no copula in equative sentences — in the opposite direction from what substrate transmission would predict. If the bioprogram features survive even when the superstrate is non-European and the substrate is non-European, Mufwene's ecology account cannot explain the convergence. The Ki-Nubi and Juba Arabic data supports Bickerton: SVO and copula optionality emerge in creolisation regardless of superstrate typology. The compression implication: SVO and copula optionality are robust enough across ecologically diverse creoles to be treated as genuine universals for compression purposes.

**Resolution of Clash 2:** Mufwene weakens Bickerton's claim about TMA preverbal placement (which is superstrate-predictable in many cases) but does not undermine the core features — SVO, no inflection, copula optionality, preverbal negation — which survive the ecological controls. Greenberg's verdict: these four features are both universals-consistent and ecologically robust, and can be borrowed as compression principles. TMA preverbal particle placement is less universally supported and should be treated as a default, not a categorical rule.

---

## Part 3 — Revised Positions

**Bickerton (revised):** Core claim — bioprogram minimum as compression target — survives, strengthened by Greenberg's adjudication on Mufwene. The specific features with strongest cross-creole support, robust against ecological controls: SVO, no inflection, copula optionality, preverbal negation. TMA preverbal particle placement is supported for Atlantic creoles but contested for ecologically diverse cases; treat as a default. Concession to Levinson: the interaction engine provides an independent functional explanation for the same features; this confirms rather than undermines them as compression targets.

**Levinson (revised):** Core claim — I-principle default enrichment as the mechanism for safe under-specification — survives. The 200ms interaction engine evidence (Stivers et al. 2009) establishes that default completion is fast enough to support under-specification in cooperative contexts. Concession to Bickerton: the processing account does not fully explain cross-creole convergence; accept that innate preferences and processing optimality may be convergent rather than competing explanations. Revised compression principle: under-specify when the stereotypical I-principle completion is recoverable within the 200ms default window; do not under-specify when recovery requires multi-step pragmatic inference.

**Greenberg (judge, revised):** Adjudication confirmed: bioprogram core features (SVO, no inflection, copula optionality, preverbal negation) are ecologically robust; TMA preverbal particle is not universally robust. These features align with the WALS universals I identified in Round 1. Cross-round synthesis: the universals evidence (Round 1) and the creole evidence (Round 3) converge on the same compression targets, strengthening the recommendation.

**OT (judge, revised):** Constraint ranking revised to PARSE-REF >> PARSE-ARG >> MAX-INFO >> DEP-NO-FILLER >> FAITH-GRAMMAR >> AGREE. The proto-language evidence (Bickerton 2009) splits PARSE into referential and argument-structural components. The interaction engine evidence (Levinson 2016) constrains which FAITH-GRAMMAR violations are acceptable: those recoverable by automatic I-principle enrichment within 200ms.

---

## Part 4 — Derived System Prompt Instructions

**Bickerton:** Omit copula in predicative and equative constructions, articles, and all inflectional morphology — verb conjugation, case, number agreement — as these are absent in the grammatically stable minimum that emerges when untrained speakers build language from scratch under communicative pressure (Bickerton 1984; confirmed cross-ecologically against Mufwene's ecology model for SVO, copula optionality, and no inflection); use SVO order throughout and mark negation with a preverbal particle.

**Levinson:** Under-specify descriptions whose stereotypical I-principle completion is the intended reading — omit copulas, articles, and grammatical morphemes when these are the default completions that fire automatically within the 200ms response-planning window (Stivers et al. 2009); do not under-specify predicate-argument structure, as argument roles are not default completions and their absence requires costly multi-step inference.

**Greenberg (judge instruction):** Treat as inviolable only those grammatical elements present in all 2,662 WALS languages (word order default; overt negation marking); treat SVO, copula optionality, and no inflection as converging bioprogram and universals evidence supporting their dispensability.

**OT (judge instruction):** Apply PARSE-REF >> PARSE-ARG >> MAX-INFO >> DEP-NO-FILLER >> FAITH-GRAMMAR >> AGREE; permit FAITH-GRAMMAR violations only when the violated element is recoverable within the 200ms I-principle default window.

---

## Part 5 — Round 3 Synthesis

**What survived cross-examination:**

1. Bioprogram core features — SVO, no inflection, no articles, copula optionality, preverbal negation — are ecologically robust (survives Mufwene's ecology challenge for these specific features) and cross-universals consistent (Greenberg).
2. I-principle default enrichment is fast enough to support grammatical under-specification — Stivers et al. (2009) 200ms window supports safe omission of morphemes recoverable as default completions.
3. Argument structure must be retained — OT's PARSE-ARG constraint; proto-language evidence shows referent listing without argument structure is insufficient for relational queries.
4. PARSE-REF >> PARSE-ARG >> MAX-INFO >> DEP-NO-FILLER >> FAITH-GRAMMAR >> AGREE — revised ranking survives.

**What was eliminated or reduced:**

- Bickerton's TMA preverbal particle placement as a categorical rule — reduced to a default on ecological grounds (Greenberg's adjudication).
- Levinson's broad claim that all GCIs fire costlessly — narrowed to I-principle stereotypical completions recoverable within 200ms; Q-implicatures and M-implicatures may be more costly.

---

### Round 3 Candidate System Prompt

> Omit copula in predicative constructions, articles, and all inflectional morphology; these are absent in the grammatically stable minimum that emerges when speakers build language without instruction (Bickerton 1984; Stivers et al. 2009 confirm these omissions are recoverable within the 200ms default enrichment window). Use SVO order throughout; mark negation with a preverbal particle. Retain full predicate-argument structure — who does what to whom — as argument roles are not default completions and their omission requires costly inference. Drop tokens in order of propositional dispensability: morphological dressing first, then connectives, then filler; propositional content last. Satisfy in order: represent all referents; represent all argument roles; include all necessary content; add no filler; then maintain grammar.
