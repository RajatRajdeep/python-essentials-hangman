# Python Essentials - Hangman

The goal of this project is to build a simple **Hangman game** with an emphasis on learning and applying foundational Python concepts like collections, functions, and modules. This project is intended for educational purposes and serves as an introduction to organizing Python code, structuring programs, and using built-in and alternative Python collections effectively.

The project has been intentionally left as a **half-baked solution**; the challenge is for you to structure the program into multiple modules, skeleton functions, and apply appropriate collections.
For the full solution, check out the `implementation` branch.

### Key Focus Areas:
- Using **Python Collections**: Explore and utilize the following:
  - `list`
  - `set`
  - `dict`
  - `tuple`
  - `namedtuple` (from the `collections` module)
  - `Counter` (from the `collections` module)
  - `deque` (from the `collections` module)
- Working with **Modules**:
  - Built-in modules: `random`, `os`, `collections`
  - Custom modules: You will create additional modules (e.g., `utils.py`) as part of the project.



### Game Overview

The game follows the traditional mechanics of Hangman:

1. **The Computer Picks a Secret Word**:
    - A random word is chosen from a predefined collection.
    - The word is represented as underscores (`_ _ _`), with each underscore representing a hidden letter.

2. **Player's Task**:
    - The player guesses **one letter at a time** to try to reveal the hidden word.
    - For each guess:
        - **Correct Guesses**: The letter is revealed in its first corresponding positions in the word.
        - **Incorrect Guesses**: The player's lives are reduced. Players start with a fixed number of lives (e.g., 5).
	- The game offers a hint to assist players in guessing the word.
  - It also displays the last three characters guessed by the player, helping them track their guesses and avoid repeating incorrect attempts.

3. **End of the Game**:
    - **Victory Condition**: If the player successfully guesses the entire word, they win! 🎉
    - **Loss Condition**: If the player runs out of lives, the game ends with a "Game Over!" 💀


### Step-by-Step Instructions to Build the Game:

1. **Define Game Constants**: Set up constants to store the game name, number of lives, screen width, and life symbol.  

2. **Create Game Status Datastore**: Develop a data structure to manage information such as remaining lives, game state, target word with hint, guessed word, and last three letters selected.

3. **Design the Game Screen**:  Implement functionality to render the game screen, displaying the current state of the game to the player.  

4. **Initiate and Run the Game**: Implement functionality to initiate and run the game loop.

5. **Build a Word Bank**:  
   Create a collection of words with hints that the game can use as potential target words.  

6. **Add Logic to Choose a Random Word**:  
   Implement functionality to select a random word from the word bank.  

7. **Handle Player Guesses and Update Game Status**:  
   Write logic to process the player’s guessed letter, validate input, and update the game status accordingly.  

### How to Run the Game

Make sure you have Python 3 installed on your system.

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-essentials-hangman.git
   cd python-essentials-hangman
   ```

2. Run the game:
   ```bash
   python3 game.py
   ```

3. Follow the instructions displayed in your terminal to guess the letters and play the game.

---

Happy Coding and Have Fun! 🚀
