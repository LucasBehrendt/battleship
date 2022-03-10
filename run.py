import random


class Colours:
    """
    Set colours to use throughout the game
    Source: https://stackoverflow.com/questions/287871/
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def welcome_page():
    """
    Displays a greeting and prompts the user to choose a name
    Ascii art source:
    https://patorjk.com/software/taag/#p=display&f=Doom&t=Battleship
    """
    print(f"""{Colours.OKBLUE}
______       _   _   _           _     _
| ___ \     | | | | | |         | |   (_)
| |_/ / __ _| |_| |_| | ___  ___| |__  _ _ __
| ___ \/ _` | __| __| |/ _ \/ __| '_ \| | '_ \.
| |_/ / (_| | |_| |_| |  __/\__ \ | | | | |_) |
\____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                        | |
                                        |_|
    {Colours.ENDC}""")
    print("=" * 50 + "\n")
    print("Welcome to Battleship! \n")


def input_name():
    """
    Get name from user and store in variable
    """
    while True:
        # global user_name
        user_name = input("Please enter your name: \n")
        if validate_name(user_name):
            print(f"\nWelcome {user_name}!\n")
            break
    return user_name


def validate_name(name):
    """
    Validate user_name, raises ValueError if name is empty
    """
    try:
        if len(name.strip()) < 1:
            raise ValueError("Please provide at least 1 character!")
    except ValueError as e:
        print(f"{Colours.FAIL}Invalid name: {e}{Colours.ENDC}")
        return False

    return True


def display_menu():
    """
    Displays the main menu from where the user can navigate
    """
    print("=" * 22 + " Menu " + "=" * 22 + "\n")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")

    while True:
        user_choice = input("\nPlease choose an option from the menu: \n")
        if user_choice == "1":
            new_game()
        elif user_choice == "2":
            instructions()
        elif user_choice == "3":
            end()
        else:
            print(
                f"{Colours.FAIL}Please choose a valid option, "
                f"between 1 and 3{Colours.ENDC}"
            )


def instructions():
    """
    Displays instructions on how to play the game
    """
    print(
        f"{Colours.BOLD}\nWelcome to a classic "
        f"game of battleship!{Colours.ENDC}\n"
        "\nYour objective is to sink your opponents ships\n"
        "before your own fleet is decimated.\n"
        "The battle area consists of a grid 8 by 8,\n"
        "and the ships are randomly placed.\n"
        "To make a guess, simply enter the coordinates\n"
        "you wish to attack and then the computer will\n"
        "make its guess.\n"
        "The first to sink all ships is the winner!\n"
        "\nGood Luck!\n"
    )
    # print("1. Lets play!")
    # print("2. Back to menu")
    while True:
        play_return = input("1. Lets play!\n2. Back to menu\n")
        if play_return == "1":
            new_game()
        elif play_return == "2":
            display_menu()
        else:
            print(
                f"{Colours.FAIL}Please choose a valid option, "
                f"either 1 or 2{Colours.ENDC}"
            )


def new_game():
    """
    Starts a new game and takes the users inputs
    """
    while True:
        size = int(input(
                        "What size do you wish the game board to be?\n"
                        "Please choose an option between 4 and 8\n"
                        ))
        if 4 <= size <= 8:
            break
        else:
            print(f"{Colours.FAIL}Please choose a valid option{Colours.ENDC}")
    while True:
        num_ships = int(input(
                        "How many ships do you wish the game board to have?\n"
                        "Please choose an option between 5 and 10\n"
                        ))
        if 5 <= num_ships <= 10:
            break
        else:
            print(f"{Colours.FAIL}Please choose a valid option{Colours.ENDC}")
    print(f"Board size: {size}. Number of ships: {num_ships}")


def end():
    """
    When user chooses exit, quits the game and prints a message.
    """
    print("\nThanks for playing! To start over,\n"
          "click the Run Program button above.")
    print(f"""{Colours.OKBLUE}
 _____                 _ _
|  __ \               | | |
| |  \/ ___   ___   __| | |__  _   _  ___
| | __ / _ \ / _ \ / _` | '_ \| | | |/ _ \.
| |_\ \ (_) | (_) | (_| | |_) | |_| |  __/
 \____/\___/ \___/ \__,_|_.__/ \__, |\___|
                                __/ |
                               |___/
    {Colours.ENDC}""")
    exit()


def main():
    """
    Run all program functions
    """
    welcome_page()
    # global user_name
    user_name = input_name()
    display_menu()


main()
