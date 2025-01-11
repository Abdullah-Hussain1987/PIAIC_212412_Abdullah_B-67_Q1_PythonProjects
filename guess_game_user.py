# PIAIC212412
# Abdullah Hussain
# Project 3: Guess the number game python project (user)

import random

#defing the funtion guess_user
def guess_user():

    # Welcome note
    print(f"Welcome to the number guessing game\n")

    # Checking if the input for low is a number
    while True:
        try:
            low = int(input("Please enter a number to define the lower range of guessing game: "))
            break

        # If it is not a number, print the error and re-enter the loop for input
        except ValueError:
            print("Invalid input! Please enter a number")

    # Defining a variable 'high' to store the higher value of guess range


    # Checking if the input for high is a number
    while True:
        try:
            high=int(input(f"Please enter a number greater than {low} to define the upper range of guessing game: "))

            # If high is lower than low, ask the user to re-enter a higher value
            if high < low:
                print(f"Please enter a number greater than {low}")
                continue
            break

        # If it is not a number, print the error and re-enter the loop for input
        except ValueError:
            print("Invalid input! Please enter a number")


        # Generating a random number betwen 'low' and 'high'
    random_number = random.randint(low,high)

        # Initializing user_guess. This variable will store the guess from user
    guess_user = 0

        # A while loop till the user guess the right number
    while guess_user != random_number:

        # Guess from user taken as input to guess_user
        guess_user=int(input(f"Guess a randon number between {low} and {high}: " ))

        # Checking if the input is within range
        if guess_user < low or guess_user > high:
            print(f"Invalid input! Number should be between {low} and {high} ")
            continue

        # If user guess is lower than randomly generated number
        if guess_user < random_number:
            print("Guess again, Your guess is too low")

        # If user guess is higher than randomly generated number
        elif guess_user > random_number:
            print("Guess again, Your guess is too high")

    # If user guess the right number
    print("Congaratulations, You guess it right")


# Calling the guess_user function
guess_user()