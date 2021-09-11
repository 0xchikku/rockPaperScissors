import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3
    Lizard = 4
    Spock = 5


def get_computer_action():
    computer = random.randint(1, len(Action))
    computer_action = Action(computer)
    return computer_action


def get_user_action():
    choice = [f"{action.value}) {action.name}" for action in Action]
    for option in choice:
        print(option)
    user_str = input('Enter Your Choice: ')
    try:
        user = int(user_str)
    except:
        print("Invalid! Enter Number.\n")
        user = get_user_action()

    if user <= len(Action):
        user_action = Action(user)
        return user_action
    print('Invalid! \n')
    return get_user_action()


def determine_winner(user_action, computer_action):
    victories = {
        # Rock wins over Scissors and Lizard
        Action.Rock: [Action.Scissors, Action.Lizard],
        # Paper wins over Rock and Spock
        Action.Paper: [Action.Rock, Action.Spock],
        # Scissors wins over Lizard and Paper
        Action.Scissors: [Action.Lizard, Action.Paper],
        # Lizard wins over Spock and Paper
        Action.Lizard: [Action.Spock, Action.Paper],
        # Spock wins over Scissors and Rock
        Action.Spock: [Action.Scissors, Action.Rock]
    }

    defeat = victories[user_action]

    if user_action == computer_action:
        print(f"Both You and Computer chose {user_action.name}, It's a Tie!\n")
    elif computer_action in defeat:
        print(
            f"Computer: {computer_action.name}, You: {user_action.name}\nYou Won!\n")
    else:
        print(
            f"Computer: {computer_action.name}, You: {user_action.name}\nComputer Won!\n")


while True:
    user = get_user_action()
    computer = get_computer_action()
    determine_winner(user, computer)
    play_again = input('Play Again? (y/n): ')
    if play_again.lower() != 'y' or 'y' not in play_again.lower():
        break
