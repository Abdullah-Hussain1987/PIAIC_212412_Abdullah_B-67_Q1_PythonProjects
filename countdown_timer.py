# PIAIC212412
# Abdullah Hussain
# Project 6: Countdown timer python project

from datetime import datetime
import time

# defining function hangman
# This function takes an input 'x' from user and count down 'x' seconds
def countdown_timer():

    while True:
        try:
            seconds = int(input('Enter time in seconds to start the count down timer: '))
            if seconds<0:
                print("Time should be positive")
                continue
            else:
                break
        except ValueError:
            print(f"Invalid input!\n")

    # If input is 0
    if seconds == 0:
        print("Count down starting....")
        print("00: 00: 00")
        print("Time's up!")

    # If input is less than 0
    elif seconds < 0:
        print("Invalid input! Enter a positive number")
        return

    # If input is greater than 0
    else:
        print("Count down starting....")
        # Calculating hours, minutes and seconds
        hr = seconds // 3600
        min = seconds % 3600 // 60
        sec = seconds % 60

        # Printing time in hr:min:sec
        print(f"{hr:02}: {min:02}: {sec:02}")

        # Loop while time >= 0
        while seconds>=0:

            # Delay of 1 second
            time.sleep(1)

            # Decrement seconds by 1
            seconds-= 1

            # Calculating hours, minutes and seconds
            hr = seconds // 3600
            min = seconds % 3600 // 60
            sec = seconds % 60
            print(f"{hr:02}: {min:02}: {sec:02}")

            # Loop esecondsits when timer reaches 0
            if(seconds==0):
                break
        print("Time's up!")


# Calling function countdown_timer'''
countdown_timer()