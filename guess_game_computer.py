# PIAIC212412
# Abdullah Hussain
# Project 2: Guess the number game python project (computer)

import random

#defing the funtion guess_computer
def guess_computer():

    # Welcome note
    print(f"Welcome to the number guessing game (computer)\n")

    # Checking if the input for low is a number
    while True:
        try:
            low = int(input("Please enter a number to define the lower range of guessing game: "))
            break

        # If it is not a number, print the error and re-enter the loop for input
        except ValueError:
            print("Invalid input! Please enter a number")

    # Checking if the input for high is a number
    while True:
        try:
            high = int(input(f"Please enter a number greater than {low} to define the upper range of guessing game: "))

            # If high is lower than low, ask the user to re-enter a higher value
            if high <= low:
                print(f"Please enter a number greater than {low}")
                continue
            break
        # If it is not a number, print the error and re-enter the loop for input
        except ValueError:
            print("Invalid input! Please enter a number")

    # Ask the computer to guess a number between 'low' and 'high'
    print(f"\nHey user! Think of a number between {low} and {high}. I'll try to guess it!")
    input("Press enter key to start")

    feedback = ''
    while (low <= high):
        if low > high:
            print(f"The response from user is contradicting!\nProgram terminating.......Try again!")
            break

        guess = random.randint(low,high)

        # Computer asking the user's feedback
        print(f"\nComputer's guess is {guess}\n")
        print("If guess is higher than your number press 'h'")
        print("If guess is lower than your number press 'l'")
        print("If guess is correct press 'c'")
        feedback = input().lower()

        while True:

            # If computer guess is higher, set high to guess-1
            if feedback == 'h':
                if guess == low:
                    print(f"Hey user, Based on your previous inputs, Number should be >= {low}")
                    feedback = input("Please enter the response again: ").lower()
                    continue
                else:
                    high = guess - 1
                    break


            # If computer guess is lower, set low to guess+1
            elif feedback == 'l':
                if guess == high:
                    print(f"Hey user, Based on your previous inputs, Number should be <= {high}")
                    feedback = input("Please enter the response again: ").lower()
                    continue
                else:
                    low = guess + 1
                    break

            elif feedback == 'c':
                    print("Hey user, I guess it right")
                    return

            else:
                feedback=input("Please enter the valid response key: 'h', 'l' or 'c': ").lower()

    if low > high:
        print(f"The response from user is contradicting!\nProgram terminating.......Try again!")
        return


# Calling the guess_computer function
guess_computer()