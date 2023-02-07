import random

print("Welcome to the number guessing game!")
print("Try to guess the secret number between 1 and 100.")

secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low, try again.")
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print("You got it! The secret number was", secret_number)

print("Thanks for playing.")
