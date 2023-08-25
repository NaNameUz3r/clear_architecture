class InvalidCommandException(Exception):
    "Raised when input command has invalid length or tokens"
    def __init__(self, message):
        self.message = message