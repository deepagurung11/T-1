# importing the random module
import random
# generate a random number between(1, 10)
secret_number = random.randint(1, 10)

# maximum attempt allowed
max_attempts = 3
#function to display a welcome message
def welcome_message():
    print("\nwelcome to the Number Guessing Game!")
    print(f"You have (max_attempts) attempts to guess the correct number.")

# function for recursive guessing
def guess_recuesive(attempts_left):
    # get user input
    guess = int(input("\nGuess the number (between 1 and 10): "))

    # check if the guess is correct
    if guess == secret_number:
        print("Congratulation! You guessed the correct number!")  
    else: 
        print(f"Wrong guess. Attempts left: {attempts_left-1}")
        if attempts_left > 1:
            #make a recursive call for another guess
            guess_recuesive(attempts_left - 1)
        else:
            print(f"\nSorry, you couldn't guess the number. The correct number was {secret_number}.")
            #calling the function
            welcome_message()
            guess_recuesive(max_attempts)
            # using id() to get memory addresses
            print(f"Memory address of Secret Number (secret_number) is: {id(secret_number)}")