# Worked Example: how one bug was found

This is the format your own findings (FINDINGS.md) should follow. It is not
graded. Read it before you start.

## The module
`notes.py` keeps a list of notes and can report a total "word count".

## Suspected
`word_count()` claims to count words. Reading it, the loop adds `len(note)` for
each note -- and `len()` on a string is the number of **characters**, not words.
That looked wrong, so it was worth a test.

## Tried
Two notes with a known number of words:

```
n.add("hello world")   # 2 words
n.add("testing")       # 1 word
n.word_count()
```

## Observed
```
>>> n.word_count()
18
```
18 is the character count (11 + 7), not the word count.

## Expected
The two notes contain 3 words in total, so `word_count()` should return **3**.
"Word count" means words separated by whitespace -- the natural reading of the
method name and docstring.

## The test
`test_notes.py` asserts `word_count() == 3`. Against the shipped code it FAILS
(returns 18). That failing test is the proof the bug is real.

## Fixed
Count words per note instead of characters:

```
total += len(note.split())
```

With that change the test passes. Notice the order: the failing test came
first, the fix second. That is exactly how the real bug hunt must be done.
