import random

def get_winning_numbers():
    return [random.randint(1, 90) for x in range(5)]
def get_user_numbers():
    user_numbers = input("Enter 5 numbers (1-90) with spaces: ").split()
    user_numbers = [int(num) for num in user_numbers]
    return user_numbers

def check_winning_numbers(user_numbers, winning_numbers):
    identical_numbers = set(user_numbers).intersection(winning_numbers)
    return identical_numbers

def baba_ijebu_game():
    print("Game started!")
    winning_numbers = get_winning_numbers()
    user_numbers = get_user_numbers()
    print(f"The winning numbers: {winning_numbers}")
    print(f"Your numbers: {user_numbers}")
    identical_numbers = check_winning_numbers(user_numbers, winning_numbers)
    if len(identical_numbers) >= 1:
        print(f"Your identical numbers are: {identical_numbers}")
    else:
        print("No matching numbers")

if __name__ == "__main__":
    baba_ijebu_game()