
#######################


#random integer from 1 to 20
import random 
correct_number = random.randint(1, 20)

print("\nWelcome quessing game. The machine has drawn numbers between 1 and 20. You have 3 guesses.")
print (correct_number)

for i in range (1,4):

    estimated_number= int(input( "Enter the guessed number between 1 and 20 \n" ))

    if correct_number == estimated_number:
        print ("right guess"),
        break
    elif correct_number > estimated_number:
        print ("The correct number is bigger")
    elif correct_number < estimated_number:
        print ("The correct number is smaller")

    print (f"You have {3-i} guesses")
   
    if i == 3:
        print (f"you didn't guess, correct number is {correct_number}")


###################

from random import randint

# Our global variables...
correct_number = randint(1, 20)
guesses_left = 3
message = ""
game_on = True

def check_correct_number(correct_number, user_guess):
    """
    This function checks whether the user guessed the correct
    number or not and whether they've run out of guesses
    and then sends an appropriate message to the user.
    """

    global game_on

    if user_guess == correct_number:
        game_on = False
        return f"YOU WON!, The number was {correct_number}!"
    elif guesses_left == 0:
        game_on = False
        return f"Unfortunately, you've run out of guesses, the number was {correct_number}"
    elif user_guess > correct_number:
        return "The number is LOWER than your guess."
    else:
        return "The number is HIGHER than your guess."

while game_on:
    print(f"You have {guesses_left} guesses left\n")
    guesses_left -= 1
    user_guess = int(input("Guess the number (an integer): "))
    message = check_correct_number(correct_number, user_guess)
    print(message)



################


# Import random library
import random

# Set a random number between 1 and 20.
number = random.randint(1, 20)

# Set the iterative variable
i = 1

# Tells user what they have to do.
print("Guess the number between 1-20 in 3 tries.\n")

# A while loop that uses the iterative variable i. After each guess if not correct, the value increases by 1.
while i <= 3:
    print("This is your guess number", i, ".\n")

    # First, the input is made integer.
    guess = int(input('Your guess: '))

    # Second, the user inputted guess is compared to the random number defined earlier.
    if guess == number:

        # If the guess is correct, user is notified that the guess was indeed correct.
        print("Congratulations! You guessed the number!")
        break
    
    # If the guess is incorrect, at this point the iterative variable is incremented by one.
    i += 1
    
    # Next, a check whether 3 guesses has been made is done so far.
    if i > 3:

        #If 3 guesses is up, the game ends, and the player loses.
        print("You did not guess the correct number in 3 guesses.")
        break

    # If user has not made 3 guesses yet, and has only guessed incorrectly, may the user try again.
    print("Your guess is wrong! Try again!\n")
