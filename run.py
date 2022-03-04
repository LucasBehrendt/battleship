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


def introduce_game():
    """
    Displays a greeting and prompts the user to choose a name
    Ascii art source:
    https://patorjk.com/software/taag/#p=display&f=Doom&t=Battleship
    """
    print(f"""{Colours.OKBLUE}
______       _   _   _           _     _
| ___ \     | | | | | |         | |   (_)
| |_/ / __ _| |_| |_| | ___  ___| |__  _ _ __
| ___ \/ _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
| |_/ / (_| | |_| |_| |  __/\__ \ | | | | |_) |
\____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                        | |
                                        |_|
    {Colours.ENDC}""")
    print("-" * 80)
    print("\nWelcome to Battleship! \n")


def main():
    """
    Run all program functions
    """
    introduce_game()


main()
