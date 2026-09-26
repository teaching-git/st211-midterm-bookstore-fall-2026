"""User accounts: registration and login."""


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
        cleaned = "".join(ch for ch in password if ch.isalnum())
        return stored is not None and stored == cleaned
