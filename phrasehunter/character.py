import re


class Character:
    def __init__(self, char):
        if len(char) != 1:
            raise ValueError("Character can only be created with a single character.")
        self.original = char
        if self.original == ' ':
            self.was_guessed = True
        else:
            self.was_guessed = False

    def check_guess(self, guess):
        Character.validate_char(guess)

        if guess.lower() == self.original or guess.upper() == self.original:
            self.was_guessed = True
            return True
        else:
            return False

    def show(self):
        if self.original == ' ':
            return self.original
        if self.was_guessed:
            return self.original
        else:
            return '_'

    def reset(self):
        self.was_guessed = False

    @staticmethod
    def validate_char(guess):
        pattern = r'^[a-zA-Z]$'
        prog = re.compile(pattern)
        if not prog.match(guess):
            raise ValueError("Guess must be a single letter between a-z or A-Z")
