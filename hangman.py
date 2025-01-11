# PIAIC212412
# Abdullah Hussain
# Hangman python project

from wordlist import wordlist
import random

# defining function hangman

def hangman():

    # Importing worldlist from another file
    import wordlist

    # Welcome note
    print(f"Welcome to Hangman!\n")
    print(f"Guess the word by suggesting letters.")

    # Assigning the words data set from a file 'wordlist' to a variable 'list_of_words'
    list_of_words = wordlist.wordlist

    # Chosing a random word from the data and storing in the variable 'word'
    word = random.choice(list_of_words)

    # Variable 'lives' to count the false tries
    lives = 6

    # Creating a set of alphabets to store the letters already guessed
    guessed_letters = set()

    # Creating a set to store the correctly guessed letters
    word_letters = set(word)

    # Hiding the actual word by replacing the each letter with '_'
    hidden_word = ["_"] * len(word)
    print(f"{hidden_word}\n")

    # A loop till lives > 0 and complete word is not guessed
    while lives > 0 and "_" in hidden_word:

        # Ask the user to guess a letter
        guess_letter = input("Guess a letter: ").lower()

        # If input is not an alphabet or more than one letter
        if len(guess_letter) != 1 or not guess_letter.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        # If input letter is already gressed previously
        if guess_letter in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter in set of 'guessed_letter'
        guessed_letters.add(guess_letter)

        # If input letter is part of word to be guessed
        if guess_letter in word:
            print("Correct guess!")

            # Loop through each position in the word
            for index in range(len(word)):
                # If the letter matches, reveal it in the hidden_word
                if word[index] == guess_letter:
                    hidden_word[index] = guess_letter
            print(f"You have {lives} lives left and you have used these letter: {guessed_letters}.")

            # Printing the current status of word
            current_word = " ".join(hidden_word)
            print(f"Current word: {current_word}\n")

        # If input letter is not a part of word to be guessed
        else:
            lives = lives -1
            print(f"Wrong guess! The letter '{guess_letter}' is not in the word")
            print(f"You have {lives} lives left and you have used these letter: {guessed_letters}.")

            # Printing the current status of word
            current_word = " ".join(hidden_word)
            print(f"Current word: {current_word}\n")

    # If all the chances are availed
    if lives == 0:
        print("You lost!")
        print("The word was: " + word)

    # If complete word is guessed successfully
    else:
        print(" ".join(hidden_word))
        print("Congratulations! You won!")

    # Asking user to play again or not
    play_again = input("Do you want to play again? ('y'/'n'): ")
    if play_again.lower() == "y":
        hangman()
    else:
        print("Thanks for playing!")

# Calling function hamgman
hangman()