def help_function():
    print("Welcome!")
    print("Type 'start' to start the game")
    print("Type 'stop' to stop the game")
    print("Type 'quit' to quit the game")
def start_function(car_started):
    if car_started:
        print("Car is already started.")
    else:
        print("Car started.")
        return True
def stop_function(car_started):
    if not car_started:
        print("Car is already stopped.")
    else:
        print("Car stopped.")
        return False
def car_game():
    car_started = False
    while True:
        command = input("Type help to get started: ").lower()

        if command == "help":
            