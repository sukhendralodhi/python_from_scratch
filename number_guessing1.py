import random

secret_number = random.randint(1,20)
guess = None
attempts = 0
max_attempts = 5

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break

    if attempts == max_attempts:
        print(f"Game over! The number was {secret_number}.")
        break