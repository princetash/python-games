import random


def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry. Too low")
        elif guess > random_number:
            print("Sorry. Too high")

    print(f"You have gussed correct. The number was {random_number}")


user_guess(10)
