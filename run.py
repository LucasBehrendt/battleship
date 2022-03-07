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
            print("start game")
            break
        elif user_choice == "2":
            instructions()
        elif user_choice == "3":
            print("exit")
            break
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
        "\nYour objective is to sink your opponents ships before\n"
        "your own fleet is decimated. The battle area consists\n"
        "of a grid 8 by 8, and the ships are randomly placed.\n"
        "To make a guess, simply enter the coordinates you wish\n"
        "to attack and then the computer will make its guess.\n"
        "The first to sink all ships is the winner!\n"
        "\nGood Luck!\n"
    )
    # print("1. Lets play!")
    # print("2. Back to menu")
    while True:
        play_return = input("1. Lets play!\n2. Back to menu\n")
        if play_return == "1":
            print("start")
            break
        elif play_return == "2":
            display_menu()
        else:
            print(
                f"{Colours.FAIL}Please choose a valid option, "
                f"either 1 or 2{Colours.ENDC}"
            )


def main():
    """
    Run all program functions
    """
    welcome_page()
    user_name = input_name()
    display_menu()


main()
