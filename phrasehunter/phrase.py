from .character import Character


class Phrase:
    def __init__(self, phrase):
        try:
            self.phrase = [Character(c) for c in phrase]
        except Exception:
            print("You did something bad. I don't know what it is. Maybe you "
                  "tried to pass a list or an integer as a phrase or something.")
            print("Anyway, whatever you did, I don't like it. Try again when "
                  "you're willing to stop abusing your freedoms, jerk.")
            exit(1)

    def show_phrase(self):
        return ' '.join([c.show() for c in self.phrase])

    def check_guess(self, guess):
        correct = False
        for c in self.phrase:
            # print('guess', guess)
            if c.check_guess(guess):
                correct = True
        return correct

    def reset(self):
        try:
            for c in self.phrase:
                c.reset()
        except Exception:
            print('"Cannot reset. This is not my sandwich." -- Winston Churchill')
