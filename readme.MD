# Phrase Hunter

This program chooses from a list of phrases and allows player to attempt to
guess the phrase, character by character.

The player has five guesses, after which, the player will be prompted to
begin a new game.

The game can be started by creating a `Game` instance with a list of strings and
using its `start_game()` method. The
strings should consist solely of letters and spaces.
The user should be careful not to pass a list containing data types other than
strings. This has been known to make the program very angry.