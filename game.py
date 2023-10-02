import random

def get_user_choice():
    user_choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("invalid choice. Enter Rock, Paper, or Scissors: ").strip().lower()
    return user_choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins"
    
def play_again():
    return input("Play again? (yes/no): ").strip().lower() == "yes"

def RPS_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        outcome = get_winner(user_choice, computer_choice)
        print(outcome)

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    RPS_game()