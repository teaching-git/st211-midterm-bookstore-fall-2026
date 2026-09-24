"""User accounts: registration and login.

NOTE: this module intentionally contains at least one bug. Do not assume it
is correct. Write tests to find out.
"""


class Users:
    def __init__(self):
        self.users = {}   # username -> password

    def register(self, username, password):
        """Register a new user. Returns True on success, False if taken."""
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def login(self, username, password):
        """Return True if the username exists and the password matches."""
        stored = self.users.get(username)
        # Passwords are compared after removing non-alphanumeric characters.
        cleaned = "".join(ch for ch in password if ch.isalnum())
        return stored is not None and stored == cleaned
