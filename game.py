from dataclasses import dataclass, field
import random
from collections import deque, Counter
from utils import clear_screen
from constants import GAME_CONSTANTS, GAME_STATE, WordEntity


@dataclass
class GameStatus:
    state: GAME_STATE = GAME_STATE.NOT_STARTED
    lives_remaining: int = GAME_CONSTANTS.lives
    masked_word: list[str] = field(default_factory=list)
    target: WordEntity | None = None
    recent_guesses: deque = field(default_factory=lambda: deque(maxlen=3))


game_status = GameStatus()


def render_game_screen():
    clear_screen()

    print("-" * GAME_CONSTANTS.screen_width)
    print(f"{GAME_CONSTANTS.name:^{GAME_CONSTANTS.screen_width}}")
    print(
        f"{(GAME_CONSTANTS.life_symbol + ' ') * game_status.lives_remaining:>{GAME_CONSTANTS.screen_width}}"
    )
    if game_status.state == GAME_STATE.IN_PROGRESS:
        print(f"{' '.join(game_status.masked_word)}")
        print(f"{game_status.target.hint} 💡")
        print(f"Recent Guessed Letters: {', '.join(game_status.recent_guesses)}")
    elif game_status.state == GAME_STATE.VICTORY:
        print(f"🎉 You Won! You solved the word: {game_status.target.text} 🎉")
    elif game_status.state == GAME_STATE.DEFEAT:
        print(f"💔 Game Over! The word was: {game_status.target.text}")


def get_guessed_letter() -> str:
    while True:
        guess = input("Enter an alphabetic character: ").strip().upper()
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print(
                "Invalid input! Please enter a single alphabetic character. Try again..."
            )


def get_guess_letter() -> WordEntity:
    return random.choice(GAME_CONSTANTS.word_bank)


def set_guess_letter(target_word: str, masked_word: list[str], letter: str) -> None:
    for i in range(len(target_word)):
        if target_word[i] == letter and masked_word[i] == "_":
            masked_word[i] = letter
            break


def process_guess(guess: str) -> None:
    target_counter = Counter(game_status.target.text)
    guessed_counter = Counter(
        [letter for letter in game_status.masked_word if letter != "_"]
    )
    remaining_counter = target_counter - guessed_counter

    if remaining_counter[guess] > 0:
        set_guess_letter(game_status.target.text, game_status.masked_word, guess)
        guessed_counter[guess] += 1
    else:
        game_status.lives_remaining -= 1

    game_status.recent_guesses.append(guess)
    if target_counter == guessed_counter:
        game_status.state = GAME_STATE.VICTORY
    elif game_status.lives_remaining == 0:
        game_status.state = GAME_STATE.DEFEAT


def initiate_game():
    render_game_screen()
    input("Press a key to START the game...")
    game_status.state = GAME_STATE.IN_PROGRESS
    game_status.target = get_guess_letter()
    game_status.masked_word = list("_" * len(game_status.target.text))


def main():
    initiate_game()

    while game_status.state not in [GAME_STATE.VICTORY, GAME_STATE.DEFEAT]:
        render_game_screen()
        guess = get_guessed_letter()
        process_guess(guess)
    render_game_screen()


if __name__ == "__main__":
    main()
