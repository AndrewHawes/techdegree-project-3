import random

from .phrase import Phrase


class Game:
    max_guesses = 5

    def __init__(self, phrases):
        self.phrases = phrases
        self.current_phrase = Phrase(random.choice(self.phrases))

    def new_game(self):
        self.current_phrase = Phrase(random.choice(self.phrases))

    def start_game(self):
        guesses = []
        incorrect = []
        while True:
            phrase = self.current_phrase.show_phrase()
            print(phrase)
            guess = input('Please guess a letter: ')
            if guess in guesses:
                print("You've already guessed {}. Please try again.".format(guess))
                continue

            try:
                correct = self.current_phrase.check_guess(guess)
            except ValueError:
                print("Guess must be a single character between a-z or A-Z.")
                continue

            guesses.append(guess)
            if not correct:
                incorrect.append(guess)
                if len(incorrect) >= self.max_guesses:
                    print("You're out of guesses!")
                    again = input("Would you like to play again? [y]es/[n]o: ")
                    if again.lower().startswith('y'):
                        self.new_game()
                        self.start_game()
                        break
                    else:
                        break
            if '_' not in self.current_phrase.show_phrase():
                print("Congratulations! You win!")
                again = input("Would you like to play again? [y]es/[n]o: ")
                if again.lower().startswith('y'):
                    self.new_game()
                    self.start_game()
                    break
                else:
                    print("That's okay. I didn't want to play with you anymore anyway.")
                    break

            print("You have {} out of {} guesses remaining.".format(self.max_guesses - len(incorrect),
                                                                    self.max_guesses))