"""The failing test that catches the worked-example bug.

Run it:  pytest worked_example/test_notes.py
It FAILS against notes.py as shipped -- that is the point. A regression test
that fails is a test that has detected something.
"""
from worked_example.notes import Notes


def test_word_count_counts_words_not_characters():
    """Author: (worked example). word_count() should count WORDS, but returns a
    character count instead."""
    n = Notes()
    n.add("hello world")      # 2 words, 11 characters
    n.add("testing")          # 1 word,  7 characters
    # correct total is 3 words; the shipped code returns 18 (characters)
    assert n.word_count() == 3
