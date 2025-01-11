# PIAIC 212412
# Abdullah Hussain
# Project 7: Password Generator Python Project


import random
import string

# Defining a function password_generator to gnerate a random password
def password_generator():

    # Initializing a string of digits
    digits = string.digits

    # Initializing a string of symbols/special characters
    symbols = string.punctuation

    # Initializing string of upper case letters
    cap_letters = string.ascii_uppercase

    # Initializing string of lower case letters
    lower_letters = string.ascii_lowercase

    # A while to take valid input in digits for length of password
    while True:
        try:
            length = int(input("Enter length of password to be generated (minimum 6): "))

            # If length of password < 6, again ask for input
            if length < 6:
                print("Password length should be greater than 6")

            # else break this loop and proceed
            else:
                break

        # Generate a valu error if input is non integer
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # To make password strong:
    # Randomly generating a four letter string
    # With 1 capital letter, 1 small letter, 1 digit and 1 special character
    password = random.choice(cap_letters) + random.choice(lower_letters) + random.choice(digits) + random.choice(symbols)

    # A for loop to complete the password till length of password
    for i in range(length-4):
        password += random.choice(cap_letters + lower_letters + digits + symbols)

    # Again randomly shuffling the password to generate a more random password
    password = ''.join(random.sample(password, len(password)))

    # Printing the password
    print(f"Your randomly generated password is: {password}")

# Calling the function
password = password_generator()
