import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("Guess a number between 1 and 100")

while True:
    guess = input("Enter your guess (or q to quit): ")

    if guess.lower() == "q":
        print("Game exited.")
        break

    if not guess.isdigit():
        print("Please enter a number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("It’s more than that ")
    elif guess > secret_number:
        print("TIt’s less than that")
    else:
        print(f"Correct! You guessed it in {attempts} attempts 🎉")
        break
