from typing import NamedTuple
import enum


class WordEntity(NamedTuple):
    text: str
    hint: str


class GameConstants(NamedTuple):
    name: str = "Hangman with 🐍"
    lives: int = 5
    life_symbol: str = "❤️"
    screen_width: int = 80
    word_bank: tuple[WordEntity, ...] = (
        WordEntity("PYTHON", "Not the snake, but you’ll definitely debug its bites"),
        WordEntity("ARRAY", "If you’re lost, just index your way out!"),
        WordEntity("LOOP", "Round and round we go, where it ends, nobody knows"),
        WordEntity("BINARY", "It’s all 1s and 0s—unless there’s a typo in your logic"),
        WordEntity(
            "SYNTAX", "It’s like grammar... but mess it up, and the compiler screams"
        ),
    )


GAME_CONSTANTS = GameConstants()


class GAME_STATE(enum.StrEnum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    VICTORY = "VICTORY"
    DEFEAT = "DEFEAT"
