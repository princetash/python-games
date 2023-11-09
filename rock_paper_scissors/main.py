import random


def play():
    user_choice = input("Rock , Paper, Scissors : ").lower()
    computer_choice = random .choice(['rock', 'paper', 'scissors'])

    if user_choice == computer_choice:
        return f'Its a tie \nComputer :{computer_choice}, \nUser: {user_choice}'

    if is_win(user_choice, computer_choice):
        return f'you won \nComputer :{computer_choice}, \nUser: {user_choice}'

    return f"Computer wins \nComputer :{computer_choice}, \nUser: {user_choice}"


def is_win(player, opponnent):
    if (player == 'rock' and opponnent == 'scissors') or \
        (player == 'scissors' and opponnent == 'paper') or \
            (player == 'paper' and opponnent == 'rock'):
        return True


print(play())
