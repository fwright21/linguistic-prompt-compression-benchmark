# Shared Questions for All Agents

Every agent must answer all five questions. This allows direct comparison across frameworks and keeps agents focused on the actual goal: output token reduction.

---

## The five shared questions

### 1. What does caveman drop that your framework says is actually necessary?

Be honest. Caveman drops a lot. Some of what it drops genuinely hurts comprehension — the output is parseable but at a cost. Identify specifically what caveman removes that your framework would say must be kept for the output to be recoverable and usable.

---

### 2. What does caveman keep that your framework says could also be dropped?

This is the key question for beating caveman. Caveman is not maximally compressed — it still contains tokens that a more sophisticated approach could remove. Identify what those tokens are and why your framework says they are expendable.

---

### 3. What system prompt instruction, in one sentence, would produce shorter output than caveman?

One sentence. Actual instruction text. Not a description of a principle — the instruction itself. This must be something a user could paste into a system prompt field and expect Claude to follow.

---

### 4. What is the minimum a response needs to contain to be recoverable and usable?

Define the floor. Below this floor, output is too short to be useful — the user cannot understand what Claude meant or cannot act on it. What exactly is that floor? Be specific: which elements of a response are strictly necessary for it to count as a valid response?

---

### 5. Where does caveman fail — produces output that is too short to be useful?

Caveman overcorrects on some query types. Identify the cases where caveman output is so compressed that it fails — where the user would not be able to understand or use the response. These are the cases where a better prompt can be shorter than caveman on easy queries while being longer where it needs to be.
