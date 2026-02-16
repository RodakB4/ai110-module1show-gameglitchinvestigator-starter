import random


def reset_session(session_state, low, high):
    """Reset all game session state for a new game."""
    session_state.secret = random.randint(low, high)
    session_state.attempts = 0
    session_state.score = 0
    session_state.history = []
    session_state.status = "playing"


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

#Bug: Need to change hint so that it says to low when number is below Secret and too high when the number is above secre.
#Fix: Hint now displays higher and lower correctly using claude's chat bot.
def check_guess(guess, secret):
    """Compare guess to secret and return (outcome, message)."""
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
