# PIAIC212412
# Abdullah Hussain
# Rock, paper, scissors python project

import random
# Defing the funtion rock_paper_scissors
def rock_paper_scissors():

    # Welcome note
    print("Welcome to Rock, Paper, Scissors")

    # Defining the three possible choices (rock, paper and scissors)
    choices = {
        "r": "rock",
        "p": "paper",
        "s": "scissors",
    }

    while True:
        # Asking user to enter a choice (rock, paper or scissors)
        user_choice = input("Enter a choice ('r' for rock, 'p' for paper, 's' for scissors): ").lower()

        # If user input is invalid
        if(user_choice not in choices):
            print("Invalid choice. Please try again.")
            continue

        # Asking computer to randomly choice between rock, paper and scissors
        computer_choice = random.choice(['r','s','p'])

        # Printing user choice and computer choice
        print(f"\nYou chose: {choices[user_choice]}. \nComputer chose: {choices[computer_choice]}.\n")

        # If user and computer choices are same, It's a tie!
        if(user_choice == computer_choice):
            print("It's a tie!")

        elif(user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")

        else:
            print("Computer wins!")

        # Asking user to play again or not
        print("Press 'y' if you want to play again")
        play_again = input().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Calling function rock_paper_scissors
rock_paper_scissors()