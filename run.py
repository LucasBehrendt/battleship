"""
Import random to generate random integers in game.
Import os to clear window in game.
"""
from random import randint
import os


class Colours:
    """
    Set colours to use on text throughout the game.
    Source: https://stackoverflow.com/questions/287871/
    """
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def welcome_page():
    """
    Displays a greeting.
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
    Ask the user for a name and stores it
    in a global variable to be used in the game.
    """
    while True:
        global user_name
        user_name = input("Please enter your name: \n")
        if validate_name(user_name):
            print(f"\nWelcome {user_name}!\n")
            break


def validate_name(name):
    """
    Validates user_name, raises ValueError if name is empty
    or only consists of space(s).
    Parameter:
        name: Takes user_name input.
    Return:
        True if input is valid, False if not.
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
    Displays the main menu from where the user can either
    start the game, receive instructions on how to play,
    or exit the program. Prints a message if the input
    is not valid, asking for a valid option.
    Clear window source: https://stackoverflow.com/questions/2084508/
    """
    print("=" * 22 + " Menu " + "=" * 22 + "\n")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")

    while True:
        user_choice = input("\nPlease choose an option from the menu: \n")
        if user_choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            new_game()
        elif user_choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            instructions()
        elif user_choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            end()
        else:
            print(
                f"{Colours.FAIL}Please choose a valid option, "
                f"between 1 and 3{Colours.ENDC}"
            )


scores = {"computer": 0, "user": 0}


class GameBoard:
    """
    Main class to create game boards. Sets board size,
    number of ships, username and type of board(user
    or computer). Stores guesses made and the location
    of the randomized ships.
    Parameters:
        self: GameBoard being built.
        size, num_ships: User inputs.
        name: Username chosen by user.
        type: Type of player(user or computer).
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
        self.board = [[" "] * size for i in range(size)]

    def print_board(self):
        """
        Prints the boards with rows and columns numbered,
        starting at 0 and a header showing who owns the board.
        Essentially joins rows of board defined in __init__.
        Source of the print gameboard loop:
        https://www.youtube.com/watch?v=alJH_c9t4zw&t=324s
        Parameters:
            self: GameBoard being built.
        """
        if self.type == "user":
            print(f"\n{self.name}'s gameboard")
        elif self.type == "computer":
            print("Computer gameboard")
        col_numbers = list(range(0, self.size))
        col_str = [str(i) for i in col_numbers]
        print("  " + " ".join(col_str))
        row_number = 0
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1
        print("")

    def guess(self, row, col):
        """
        Checks whether the guess is a hit or miss and
        saves all guesses in guesses variable.
        Prints 'X' for hit and '-' for miss.
        Inspired by Code Institute scope video.
        Parameters:
            self: GameBoard being built.
            row, col: Coordinate inputs from user.
        Return:
            'Hit' if a ship is sunk, 'Miss' if not.
        """
        self.guesses.append((row, col))
        if (row, col) in self.ships:
            self.board[row][col] = "X"
            return "Hit"
        else:
            self.board[row][col] = "-"
            return "Miss"

    def add_ship(self, row, col, type="computer"):
        """
        Places ships on the board with the help
        of randomized coordinates passed in from
        populate_board.
        When placing on the users board, assigns
        a '@' to mark the location.
        Inspired by Code Institute scope video.
        Parameters:
            self: GameBoard being built.
            row, col: Random coordinates for appending ships.
            type: Type of player(user or computer).
        """
        if len(self.ships) >= self.num_ships:
            pass
        else:
            self.ships.append((row, col))
            if self.type == "user":
                self.board[row][col] = "@"


def populate_board(board):
    """
    Generates random integers as coordinates
    for the ships to be placed on. Checks for
    already placed ships so no overlapping occurs.
    Parameter:
        board: The GameBoard being populated.
    """
    for ship in range(board.num_ships):
        row = randint(0, board.size-1)
        col = randint(0, board.size-1)
        while (row, col) in board.ships:
            row = randint(0, board.size-1)
            col = randint(0, board.size-1)
        board.add_ship(row, col)


def validate_coordinates(board, board_2, row, col):
    """
    Prints if a guess is a hit or
    a miss and increments the score.
    Parameters:
        board, board_2: Both GameBoards being validated.
        row, col: Coordinates of guesses.
    """
    shot = board_2.guess(row, col)
    if shot == "Hit":
        print(f"{board.name} hit an enemy ship!")
        scores[board.type] += 1
    else:
        print(f"{board.name} missed this time.")


def make_guess(board, board_2):
    """
    Prompts the user to make a guess on the row and
    column respectively and generates a random guess
    for the computer. Checks the user inputs to make
    sure they are correct and prints the relevant error
    message if not.
    Parameters:
        board, board_2: Both GameBoards to be guessed on.
    """
    while True:
        try:
            if board.type == "user":
                row = int(input("Guess a row: \n"))
                col = int(input("Guess a column: \n"))
                print("")
            else:
                row = randint(0, board.size-1)
                col = randint(0, board.size-1)
            if (row, col) in board_2.guesses:
                if board.type == "user":
                    print(f"{Colours.FAIL}Invalid input: You already "
                          f"guessed those coordinates!{Colours.ENDC}")
            elif 0 <= row <= board.size-1 and 0 <= col <= board.size-1:
                return row, col
            else:
                print(
                      f"{Colours.FAIL}Invalid input: The coordinates are "
                      "outside the board range,\nplease enter a number "
                      f"between 0 and {board.size-1}{Colours.ENDC}"
                     )
        except ValueError:
            print(f"{Colours.FAIL}Invalid input: "
                  f"Please enter a number{Colours.ENDC}")


def instructions():
    """
    Displays instructions on how to play the game.
    Asks the user to either start the game or go back
    to the main menu.
    Clear window source: https://stackoverflow.com/questions/2084508/
    """
    print(
        f"{Colours.BOLD}\nWelcome to a classic "
        f"game of battleship!{Colours.ENDC}\n"
        "\nYour objective is to sink your opponents ships\n"
        "before your own fleet is decimated.\n"
        "The battle area consists of a board size chosen by you,\n"
        "between 4x4 and 8x8. The number of ships can be chosen\n"
        "to be between 5 and 10 each, and are randomly placed.\n"
        "To make a guess, simply enter the coordinates\n"
        "you wish to attack, with the upper left corner being\n"
        "row 0 and column 0. The computer will then randomize a guess\n"
        "and the results of the round will be displayed.\n"
        "The ships on your board will be marked as '@' and on the\n"
        "computers board they will be hidden.\n"
        "A hit on an enemy ship will be marked with an 'X', while a miss\n"
        "will be marked as '-' on the boards.\n"
        "The first to sink all ships is the winner!\n"
        "\nGood Luck!\n"
    )
    while True:
        play_return = input("1. Lets play!\n2. Back to menu\n")
        if play_return == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            new_game()
        elif play_return == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            display_menu()
        else:
            print(
                f"{Colours.FAIL}Please choose a valid option, "
                f"either 1 or 2{Colours.ENDC}"
            )


def end():
    """
    When user chooses exit, ends the game and prints a goodbye
    message, with instructions on how to run the game again.
    Ascii art source:
    https://patorjk.com/software/taag/#p=display&f=Doom&t=Battleship
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


def new_game():
    """
    Starts a new game and takes the users inputs
    and creates boards with those parameters.
    Loops through rounds of guesses until the user
    or computer sinks all enemy ships. It then displays
    a message with the final result and takes the user
    back to the main menu.
    """
    while True:
        try:
            size = int(input(
                            "What size do you wish the game board to be?\n"
                            "Please choose an option between 4 and 8\n"
                            ))
            if 4 <= size <= 8:
                break
            else:
                print(f"{Colours.FAIL}Invalid input: Please "
                      f"choose a valid option{Colours.ENDC}")
        except ValueError:
            print(f"{Colours.FAIL}Invalid input: "
                  f"Please enter a number{Colours.ENDC}")
    while True:
        try:
            num_ships = int(input(
                            "How many ships do you wish the game board to "
                            "have?\n"
                            "Please choose an option between 5 and 10\n"
                            ))
            if 5 <= num_ships <= 10:
                break
            else:
                print(f"{Colours.FAIL}Invalid input: Please "
                      f"choose a valid option{Colours.ENDC}")
        except ValueError:
            print(f"{Colours.FAIL}Invalid input: "
                  f"Please enter a number{Colours.ENDC}")

    print(f"Board size: {size}. Number of ships: {num_ships}\n")

    user_board = GameBoard(size, num_ships, user_name, type="user")
    computer_board = GameBoard(size, num_ships, "Computer", type="computer")

    scores["computer"] = 0
    scores["user"] = 0

    populate_board(user_board)
    populate_board(computer_board)
    while True:
        print("=" * 50)
        GameBoard.print_board(user_board)
        GameBoard.print_board(computer_board)

        print("The scores are:")
        print(f"{user_name}: {scores['user']}\n"
              f"Computer: {scores['computer']}\n")

        if scores["user"] >= num_ships and scores["computer"] >= num_ships:
            print("Its a draw!")
            print("Taking you back to the main menu...\n")
            display_menu()
        elif scores["user"] >= num_ships:
            print(f"{Colours.OKGREEN}\nCongratulations! "
                  f"You won the game!{Colours.ENDC}")
            print("Taking you back to the main menu...\n")
            display_menu()
        elif scores["computer"] >= num_ships:
            print(f"{Colours.WARNING}\nGame over, "
                  f"the computer won this time!{Colours.ENDC}")
            print("Taking you back to the main menu...\n")
            display_menu()

        user_guess = make_guess(user_board, computer_board)
        user_row = user_guess[0]
        user_col = user_guess[1]
        validate_coordinates(user_board, computer_board, user_row, user_col)

        computer_guess = make_guess(computer_board, user_board)
        comp_row = computer_guess[0]
        comp_col = computer_guess[1]
        validate_coordinates(computer_board, user_board, comp_row, comp_col)


def main():
    """
    Run all program functions.
    """
    welcome_page()
    input_name()
    display_menu()


# Source of why to use: https://stackoverflow.com/questions/419163/
if __name__ == "__main__":
    main()
