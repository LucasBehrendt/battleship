# Battleship

Battleship is a Python terminal game based on the classic with the same name. It is a turn-based guessing game where you play against the computer and try to sink your enemies battleships before your own fleet is destroyed. The user can choose both the grid size and the number of ships to be deployed on each board.

By developing the game on Code Institutes Python Template, it can be run in a web browser, as opposed to only being able to run on a CLI or Command Line Interface.

[Find the live website here!](https://battleship-pp3.herokuapp.com/)

![Responsive Image](docs/images/responsive.png)

# Table of Contents
- [Battleship](#battleship)
  * [How To Play](#how-to-play)
  * [User Experience (UX)](#user-experience-ux)
    + [Site Owner Goals](#site-owner-goals)
    + [User Goals](#user-goals)
    + [Structure](#structure)
    + [Design](#design)
  * [Flowchart](#flowchart)
  * [Features](#features)
    + [Welcome Page](#welcome-page)
    + [Main Menu](#main-menu)
    + [Game Parameters](#game-parameters)
    + [Game Boards](#game-boards)
    + [Playing The Game](#playing-the-game)
    + [Instructions Page](#instructions-page)
    + [Exit Page](#exit-page)
    + [Future Features](#future-features)
  * [Data Model](#data-model)
  * [Testing](#testing)
    + [Validator Testing](#validator-testing)
    + [Lighthouse Testing](#lighthouse-testing)
    + [Manual Testing](#manual-testing)
    + [Fixed Bugs](#fixed-bugs)
    + [Known/Unfixed Bugs](#knownunfixed-bugs)
  * [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Programs & Libraries](#programs--libraries)
  * [Deployment](#deployment)
    + [Heroku](#heroku)
    + [Cloning](#cloning)
  * [Credits](#credits)
    + [Code](#code)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## How To Play

Battleship is a board game where the objective is to sink all your opponents ships before your own ships are destroyed. This version of the game lets the user first enter a name and then gets taken to the main menu, where they can choose to jump straight into the game, read instructions on how to play or exit the game. When starting a new game, the user chooses a board size between 4x4 and 8x8 to play against the computer on. The user is also asked to input how many ships are to be deployed, between 5 and 10 on each board. With the parameters set, the boards are created and populated with randomly placed ships. The user and computer then take turns guessing coordinates to try and hit each others ships. The users ships are marked with '@' while the computers ships are hidden. A hit on an enemy ship is marked with 'X' and a miss is marked with '-'. The first to sink all enemy ships is the winner!

To read more about the game rules, please visit this [Wikipedia page](https://en.wikipedia.org/wiki/Battleship_(game)).

## User Experience (UX)
### Site Owner Goals

- Develop a fun and well-functioning mini game in a CLI environment.

- Provide a simple and intuitive navigation throughout the game and give the user a positive overall impression.

- Give the user the choice to modify the game board and number of ships, to keep the user engaged over more than a single game.

- Write clean and readable code on which the game runs, and make sure the game doesn't break on any user inputs.

### User Goals

- Understand the purpose and navigation of the game instantly.

- Play a fun and simple game against the computer.

- View game rules and understand the logic of the game easily.

- See the current score in mid game and view the game boards after each turn.

- Change parameters of the game to play multiple times and have different experiences.

### Structure

The structure of the game is kept simple and intuitive to make sure the user can easily navigate the game and have a positive experience. The main menu works as a hub from where the user can access the different points of the game, and when a game is finished the user is taken back to the menu. By keeping the structure simple and not too clotty, there is a pleasing flow to the game. If desired, a game of Battleship can be played in just a few minutes to reach as wide an audience as possible.

### Design

As the game is developed for a CLI environment there is no traditional design features present, aside from the text being coloured to fit some particular messages. For example, all error messages are red, and some ASCII art are coloured blue.

## Flowchart

The flowchart was created using [Lucidchart](https://www.lucidchart.com/pages/).

<details>

<summary>Flowchart</summary>

![Flowchart](docs/images/flowchart.png)

</details>

## Features

In the following section I will provide an overview of the features included in Battleship. The game is built on the Code Institute Python Template, which provides the HTML and CSS code necessary to play the game in a browser. As that code is not written by the developer, its features will not be mentioned.

### Welcome Page

- The welcome page consists of the name of the game 'Battleship' presented as ASCII art and a small welcome message. 

- The user is then prompted to enter a name, which is validated to be at least one character. If left blank, an error message will print, asking for a valid input.

<details>

<summary>Welcome Page image</summary>

![Welcome Page](docs/images/welcome-page.png)

</details>

<details>

<summary>Invalid name image</summary>

![Invalid name](docs/images/invalid-name.png)

</details>

### Main Menu

- After a valid name is received, the main menu is displayed. From here the user can navigate to different points in the game.

- To start the game, the user simply types 1. Instructions on how to play can be found by typing 2. If the user wishes to exit the game, they type 3.

- If an invalid input is received, an error message with instructions on valid inputs is printed.

<details>

<summary>Main Menu image</summary>

![Main Menu](docs/images/main-menu.png)

</details>

<details>

<summary>Main Menu image - invalid input</summary>

![Main Menu invalid](docs/images/menu-invalid.png)

</details>

### Game Parameters

- When starting a new game, the user is asked to choose the game board size and number of ships to be deployed.

- If the user inputs invalid parameters a relevant error message will be displayed that lets the user type a valid option.

- When the choices are made, the board size and number of ships are printed out and the game begins.

<details>

<summary>Game Parameters image</summary>

![Game Parameters](docs/images/game-parameters.png)

</details>

<details>

<summary>Game Parameters image - invalid input</summary>

![Game Parameters invalid](docs/images/game-parameters-invalid.png)

</details>

### Game Boards

- When parameters are set, the game boards are printed out and populated with the specified number of ships.

- The ships are randomly assigned to both boards and are checked to make sure they don't overlap.

- Numbers are printed along the rows and columns to help the user easier find the coordinates.

- The ships are marked as '@' on the users board and, for obvious reasons, they are hidden on the computers board.

- Beneath both boards, the current score is displayed.

<details>

<summary>Game Boards image</summary>

![Game Boards](docs/images/game-boards.png)

</details>

### Playing The Game

- After the boards and scores are printed, the user is prompted to make a guess where an enemy ship might be. First, they input a row number, followed by a column number.

- If the user input doesn't match the expected input an error message is displayed, with the relevant information. If a user tries to guess coordinates already guessed, a message informing them of this will be displayed.

- The computer then generates a random guess and tries its luck before the results are shown and the next turn begins.

- A short message declaring a hit or miss by either side is displayed before the updated game boards and scores are printed again.

- If a hit is made by either side, the enemy board receives an 'X' to mark a sunken ship. A miss will result in a '-' to mark a previously missed guess.

- As the game progresses the boards will fill with hit and miss symbols until either a winner is declared, or a draw occurs. When all ships on either board are sunk, the game ends and the user is taken back to the main menu, where they can start again with new parameters if they wish.

<details>

<summary>User Guess image - invalid input</summary>

![User Guess invalid input num](docs/images/game-invalid-num.png)
![User Guess invalid input letter](docs/images/game-invalid-letter.png)
![User Guess invalid input guessed](docs/images/game-invalid-guessed.png)

</details>

<details>

<summary>User Guess image - Miss</summary>

![User Guess miss](docs/images/game-miss.png)

</details>

<details>

<summary>User Guess image - Hit</summary>

![User Guess hit](docs/images/game-hit.png)

</details>

<details>

<summary>Game Won image</summary>

![Game Won 1](docs/images/game-won-1.png)
![Game Won 2](docs/images/game-won-2.png)

</details>

<details>

<summary>Game Draw image</summary>

![Game Draw 1](docs/images/game-draw-1.png)
![Game Draw 2](docs/images/game-draw-2.png)

</details>

<details>

<summary>Game Over image</summary>

![Game Over 1](docs/images/game-over-1.png)
![Game Over 2](docs/images/game-over-2.png)

</details>

### Instructions Page

- From the main menu, the user can navigate to the instructions page by typing 2. Here the user will learn how the game operates and takes input. 

- When the user is ready, they can start a new game straight from this page, or they can choose to go back to the main menu.

- If an invalid input is received, an error message with instructions on valid inputs is printed.

<details>

<summary>Instructions Page image</summary>

![Instructions Page](docs/images/instructions.png)

</details>

<details>

<summary>Instructions Page image - invalid input</summary>

![Instructions Page invalid](docs/images/instructions-invalid.png)

</details>

### Exit Page

- When a user chooses to exit the game from the main menu, a small message thanks the user for playing and prints the word 'goodbye' in ASCII art. The user is also informed to press the 'Run Program' button to restart the game.

<details>

<summary>Exit Page image</summary>

![Exit Page](docs/images/exit.png)

</details>

### Future Features

- Ships that take up more than one grid size, much like the original game.

- High score system through a Google Spreadsheet.

- Two-player function to play against another user either locally or online.

- A properly designed UI to add to the experience.

## Data Model

- The game utilizes a GameBoard class to create both boards, in which the input parameters, such as size and number of ships are stored. It also takes in all guesses made on each board, the location of the deployed ships, the name and type of player the board belongs to (user or computer).

- The class then builds the boards with the correct parameters and prints them out. After each turn the boards are updated with the stored guesses and printed out anew.

- Aside from the GameBoard class there are helper functions that are called as the game progresses, such as asking for and validating the coordinates guessed and generating random integers to use when adding the ships.

## Testing
### Validator Testing

- To ensure that the python code is free of errors and written correctly, validation through the PEP8 online validator was performed with no errors or warnings raised.

<details>

<summary>PEP8 Online Validator</summary>

![PEP8 Online Validator](docs/images/pep8-validator.png)

</details>

- All HTML and CSS code for this game was taken from the Code Institute Python Template and has not been altered in any way. Therefore, any testing on this code will not be performed.

### Lighthouse Testing

- The Lighthouse tool in Chrome DevTools was used to mainly test the games performance and to make sure there were no performance issues when running the game. It performed well in the test, indicating a smoothly running game. 

- The issues raised in the lighthouse test, mainly in accessibility and SEO was due to code in the template and is not affected by the python code written by the developer.

<details>

<summary>Lighthouse Report</summary>

![Lighthouse Report](docs/images/lighthouse.png)

</details>

### Manual Testing

- Extensive manual testing was done throughout the developing process, where all user inputs have the desired effect. If a user input is invalid, a relevant error message will tell the user what to input instead.

- All features respond as expected and give the correct error messages when user input is invalid. Messages will be displayed in a red text colour to make sure that the user understands that an input error has occurred. To see the different messages, please check the features section.

- The game was also tested to make sure that the different parameters the user can choose will work as expected, so that the game boards will have the desired size and number of ships. The ship placement has been checked to make sure that no overlapping occurs and that all ships are deployed correctly. The computer inputs have been tested to make sure no duplicate guesses or other issues occur that are outside the control of the user. 

- Testing was performed in both the Gitpod terminal and Code Institutes Heroku mock terminal in several different browsers, such as Chrome, Edge and Firefox.

### Fixed Bugs

- The game boards initially started the rows and columns count on 1. This created some issues when validating user and computer coordinates. By changing to starting at 0, they match the coordinates created when an input is made, as they start with 0-index.

- There was a validation issue with duplicate guesses. The turn continued instead of asking for a new guess. A solution was found by moving duplicate guess validation from validate_coordinates to make_guess inside the loop, so that if a duplicate guess is made, the user is prompted to make another guess inside the same loop as the user inputs are in.

- User guesses returned a list while computer guesses returned a tuple as expected. An incorrect append to guesses in validate_coordinates was removed, as it was mistakenly placed there, and the append instead happens in the guess function.

- When populating the boards, computer board ships overlapped because of an if statement checking for already added '@'. By changing to check if coordinates are in ships list, the issue was resolved.

- Bad error message when user input was not integer. The ValueError raised was printed incorrectly. By changing the print statements in the error handling, the desired output is now received.

### Known/Unfixed Bugs

- As of writing this readme, no known bugs remain unfixed.

## Technologies Used
### Languages

- [Python](https://www.python.org/)

#### Python Libraries

- [OS](https://docs.python.org/3/library/os.html) - A Python library used for clearing the window at certain points in the game.

- [Random](https://docs.python.org/3/library/random.html) - A Python library used to generate random integers in the game.

### Programs & Libraries

- [Git](https://git-scm.com/) - Git was used through the Gitpod terminal to commit to Git and push to GitHub.

- [GitHub](https://github.com/) - All code for the site is stored on GitHub after being pushed from Git.

- [Heroku](https://www.heroku.com) - Used for hosting the game.

- [Lucidchart](https://www.lucidchart.com/pages/) - The flowchart created for the game was made through Lucidchart.

- [Patorjk ASCII Art Generator](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - The ASCII art used in the game was generated with this app.

- [PEP8 Online Validator](http://pep8online.com/) - Validation of Python code was done with PEP8 Online.

- [Techsini](http://techsini.com/multi-mockup/index.php) - The responsive image at the top of the README came from Techsini.

## Deployment
### Heroku

The game was deployed using Heroku. The steps for the deployment process are:

1. If any installs or packages were made for the project, make sure they are added to the requirements.txt file.

2. To do this, simply type `pip3 freeze > requirements.txt` in the terminal and the file will be updated.

3. Make sure the updated and newest version of the project is pushed to GitHub.

4. Go to Heroku's website at https://www.heroku.com and sign up/log in.

5. Click on the **New** button near the top right corner, and select **Create new app**.

6. Name the project and set the region to the relevant one, then click the **Create app** button.

7. When the app has been created, go to the **Settings** tab. Scroll down to **Config Vars** and click on **Reveal Config Vars**.

8. Add the relevant Config vars for your project. For this game there are no API:s or CREDS so the only necessary one is Key: PORT and Value: 8000. 

9. Below **Config Vars** you will find the **Buildpacks** section. Click on **Add buildpack** and add **Python**, click **Save changes**. Repeat the process for **nodejs** and make sure they are in the correct order, with **Python** coming first.

10. Next, navigate to the **Deploy** tab and under **Deployment method** connect to your GitHub account.

11. Directly below **Deployment method** there is a search bar to search for your repository. Connect the correct one to Heroku by clicking the **Connect** button.

12. Scroll down to **Manual deploy** and click **Deploy Branch**, making sure that the main branch is selected.

13. To enable automatic updates to the project, simply scroll up to **Automatic deploys** and click the **Enable Automatic Deploys** button.

14. Your project is now hosted on Heroku, and the URL can be found under the **Settings** tab, at **Domains**.

The live link can be found here - [Battleship](https://battleship-pp3.herokuapp.com/)

### Cloning

The repository for the website can be cloned to a local machine. The cloning procedure pulls down a full copy of all the data on GitHub.com at that time. The steps required for the clone are:

1. Navigate to the main page of the repository you wish to clone.

2. Above the list of files, click the "code" button.

3. To clone the repository using HTTPS, under "clone with HTTPS", copy the URL provided.

4. Open Git Bash.

5. Change the current working directory to the location where you want the cloned directory.

6. Type `git clone`, and then paste the URL you copied earlier.
     ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`
    ```
7. Press Enter to create your local clone.
    ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    > Cloning into `Clone-dir`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    ```
For a more detailed explanation, see this [walkthrough](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Credits
### Code

All code used in the game that is not the developers is credited in code comments. The sources are listed below.

- [Stackoverflow](https://stackoverflow.com/) was a great source of inspiration and helped me with several solutions throughout the game such as:

  - Printing coloured text came from [this post](https://stackoverflow.com/questions/287871/).

  - How to use the os.system clear command was taken from [this post](https://stackoverflow.com/questions/2084508/).

  - The reason for using `if __name__ == "__main__"` came from [this post](https://stackoverflow.com/questions/419163/)

- The print board loop in print_board was taken from [this YouTube video](https://www.youtube.com/watch?v=alJH_c9t4zw).

- [W3Schools](https://www.w3schools.com/) helped with mainly syntax issues and was very helpful when something wasn't acting as expected.

- The Code Institute scope video on building a battleship game was a great source of inspiration and some of the functions in this game was taken from there, including the guess function as well as the add_ship function.

- The [Code Institute Python Template](https://github.com/Code-Institute-Org/python-essentials-template) provided all the HTML and CSS code for the game.

- My mentor Brian helped me with some of the code, including how to fix an issue with error handling, clearing the terminal window, how to comment the code, and more.

[Back to top](#battleship)