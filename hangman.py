import random
from string import ascii_lowercase
from hangman_word_repository import word_list  # Imports a list of 1000 potential words
# define game options
allotted_guesses = 8
# These variables are defined in menu()
new_game = None
play_game = ""


def menu():
    while True:
        global play_game, new_game
        new_game = True
        play_game = input('Type "p" to play the game, "q" to quit: ')
        if play_game == "p" or play_game == "q":
            break


# Start of game
print("H A N G M A N")
menu()
while play_game == "p":
    # This block of code runs only once at the start of the game
    if new_game == True:
        # Reset variables
        word = random.choice(word_list)
        hidden_word = "-" * len(word)
        guesses_remaining = allotted_guesses
        guessed_letters = set()
        uncovered_letters = 0
        new_game = False
        print()
        print("Instructions:")
        print("Input a lower case letter to guess that letter")
        print("Input 'list' to see a list of all the letters you have already guessed")
    # Start of loop
    print()
    print(hidden_word + " " * (15 - len(word)) + "Lives left: {}".format(guesses_remaining))
    guess = input("Input a letter: ")
    # Displays a list of all the previously guessed letters
    if guess == "list":
        list_ = list(guessed_letters)
        list_.sort()
        print()
        print("Guessed letters: {}".format(list_))
        continue
    # Make sure the guess is valid
    if len(guess) != 1:
        print("You should print a single letter")
        continue
    if guess not in ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        continue
    if guess in guessed_letters:
        print("You already typed this letter")
        continue
    # If guess is correct, uncover the letters
    if guess in word:
        mutable_word = list(hidden_word)
        curr = -1
        # Find the index of all instances of the guessed letter, and then reveal them
        for i in range(word.count(guess)):
            curr = word.index(guess, (curr + 1))
            mutable_word[curr] = guess
            uncovered_letters += 1
        hidden_word = "".join(mutable_word)
        guessed_letters.add(guess)
        # Check the win condition
        if uncovered_letters == len(word):
            print()
            print(word)
            print("You guessed the word!")
            print("You survived!")
            print()
            menu()  # End of round
    # If guess is incorrect
    else:
        print("No such letter in the word")
        guessed_letters.add(guess)
        guesses_remaining -= 1
        # Check the lose condition
        if guesses_remaining == 0:
            print("You ran out of guesses!")
            print("You are hanged!")
            print()
            print("The word was {}".format(word))
            menu()
# End of program message
print()
print("Thanks for playing!")
