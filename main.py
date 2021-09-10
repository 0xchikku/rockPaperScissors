import random


possible_action = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_action)

while True:
    user_action = input("Rock, Paper or Scissors?:  ").lower()
    if user_action in possible_action:
        print(f"You Chose: {user_action}, Computer Chose: {computer_action}")

        if user_action == computer_action:
            print("Its a Tie")
        elif user_action == "rock":
            if computer_action == "scissors":
                print(f"You win!")
            else:
                print(f"Computer won!")
        elif user_action == 'paper':
            if computer_action == 'rock':
                print(f"You win!")
            else:
                print(f"Computer won!")
        elif user_action == 'scissors':
            if computer_action == 'paper':
                print(f"You win!")
            else:
                print(f"Computer won!")
    else:
        print(f"{user_action} is Invalid! Try Again ")

    play_again = input('Play Again? (y/n): ')
    if play_again.lower() == 'n' or 'n' in play_again.lower():
        break
