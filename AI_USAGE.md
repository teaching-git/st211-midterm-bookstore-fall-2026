# AI Usage Declaration and Comparison

Group: <your group name>
Members: <names>

---

## Part 1: Declaration (required)

List every AI tool your group used anywhere in this project, and how.

| AI tool | What we used it for |
| --- | --- |
| <e.g. Claude> | <e.g. explaining what a function should do> |
| <e.g. Gemini> | <e.g. drafting test ideas> |
| ... | ... |

(If you used no AI at all, write "None" and say how you worked instead.)

---

## Part 2: Comparison (do this AFTER your own bug hunt in FINDINGS.md)

We ran the same bug-hunt task through the following AI tools: <name at least 2>.

For each AI, we gave it: <describe what you gave it -- the code, the prompt>.

### Comparison table

| Bug (in your own words) | We found it? | AI #1 (<name>) found it? | AI #2 (<name>) found it? | Was each AI's test CORRECT? |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |

**The last column matters most.** For each AI test, say whether it GENUINELY
detects the bug (fails against the buggy code, passes when fixed) or whether it
just looks right but does not actually catch anything. State how you checked.

### Notes on what each AI got wrong or missed

<Write specific examples: a test an AI wrote that passed even against the buggy
code, a "bug" an AI invented that was not real, a real bug every AI missed, etc.>

---

## Part 3: Our verdict

- **Where our human judgement beat the AIs:** <bugs you found they missed, or AI
  tests you had to fix>
- **Where an AI caught something we had missed:** <be honest>
- **What this taught us about using AI to write tests:** <a few sentences>
