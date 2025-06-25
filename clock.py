import random

# Generate a random number between 1 and 100
B = random.randint(1, 100)

while True:
    A = int(input("Guess a number between 1 and 100: "))
    
    if A < B:
        print("Too low! Try again.")
    elif A > B:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break

print("Game over. The number was:", B)
# This code implements a simple number guessing game.
# The user is prompted to guess a number between 1 and 100