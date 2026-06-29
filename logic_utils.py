import random


def start_new_game(low: int, high: int):#The second bug we added new starting credentials so that the game starts with a clean slate
    """Return a fresh game state for a new round.

    Resets every piece of game state (not just secret/attempts) so a new
    game can be started after a win or loss.
    """
    return {
        "attempts": 0,
        "secret": random.randint(low, high),
        "score": 0,
        "status": "playing",
        "history": [],
    }


def record_guess(history, value):
    """Append a guess to history and return the updated list.

    Returns a new list (does not mutate the input) so the caller assigns the
    result back to session state in the same run, keeping the displayed
    history in sync with the latest guess instead of one step behind.
    """
    return history + [value]


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):# we changed the logic of the if statments and took off the try and catch exception because it would change the guess into a string and would cause the error
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
