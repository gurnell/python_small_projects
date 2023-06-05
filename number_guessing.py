# import random module
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Number of attempts the player has
max_attempts = 5
attempts = 0

print('''Are you a champion guesser?
Welcome to the Number Guessing Game!''')
print('''To get us started...I am thinking of a number between 1 and 100.
Can you guess what this number is?''')

while attempts < max_attempts:
    # prompt the player to enter their guess
    guess = int(input("Take a guess: "))

    # Increase the number of attempts
    attempts += 1

    # compare the guess with the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        # the player guessed the right number
        print("Congratulations!! You guessed the number in {} attempts".format(attempts))

# The player used up all their attempts without getting the correct number
if attempts == max_attempts:
    print("Oh No! Game over! The number I was thinking of {}.".format(secret_number))

