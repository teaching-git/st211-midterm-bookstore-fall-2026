"""A tiny note-keeper, used as the worked example. It contains ONE bug.

This module is not part of the bookstore and is not graded. It exists so you
can see a complete bug hunt -- the code, the test that catches the bug, and the
write-up -- before you start on the real thing.
"""


class Notes:
    def __init__(self):
        self.notes = []

    def add(self, text):
        """Add a note. Returns the new note count."""
        self.notes.append(text)
        return len(self.notes)

    def word_count(self):
        """Return the total number of words across all notes."""
        total = 0
        for note in self.notes:
            total += len(note)
        return total
