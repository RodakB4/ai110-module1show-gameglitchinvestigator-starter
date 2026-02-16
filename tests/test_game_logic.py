import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess
from app import update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_normal_difficulty_attempt_tracking():
    """Simulate Normal difficulty (6 attempts): last guess is processed and game-over triggers correctly."""
    secret = 50
    attempt_limit = 6  # Normal difficulty

    attempts = 0
    status = "playing"

    # --- First 5 guesses: all wrong, game should stay active ---
    for guess_num in range(1, attempt_limit):
        outcome, message = check_guess(secret - 1, secret)
        assert outcome == "Too Low"

        # Game-over check (mirrors app.py line 152)
        if attempts + 1 >= attempt_limit:
            status = "lost"

        attempts += 1
        attempts_left = attempt_limit - attempts

        assert status == "playing", f"Game ended early on guess #{guess_num}"
        assert attempts_left == attempt_limit - guess_num, (
            f"Expected {attempt_limit - guess_num} attempts left after guess #{guess_num}, "
            f"got {attempts_left}"
        )

    # --- 6th guess (last): should be processed, THEN trigger game over ---
    outcome, message = check_guess(secret + 1, secret)
    assert outcome == "Too High", "Last guess must still be processed"

    if attempts + 1 >= attempt_limit:
        status = "lost"

    attempts += 1
    attempts_left = attempt_limit - attempts

    assert status == "lost", "Game should end after all attempts are used"
    assert attempts_left == 0, "Attempts left should be 0 when game ends"
    assert attempts == attempt_limit, "Total attempts should equal the limit"


def test_score_too_high_decreases_by_5():
    """A 'Too High' guess should reduce the score by 5."""
    score = update_score(current_score=100, outcome="Too High", attempt_number=0)
    assert score == 95


def test_score_too_low_decreases_by_5():
    """A 'Too Low' guess should reduce the score by 5."""
    score = update_score(current_score=100, outcome="Too Low", attempt_number=0)
    assert score == 95


def test_score_win_increases_by_formula():
    """A 'Win' should add points using: 100 - 10 * (attempt_number + 1), min 10."""
    # Win on attempt 0 → 100 - 10*(0+1) = 90
    assert update_score(0, "Win", 0) == 90
    # Win on attempt 2 → 100 - 10*(2+1) = 70
    assert update_score(0, "Win", 2) == 70
    # Win on attempt 8 → 100 - 10*(8+1) = 10 (would be 10, not negative)
    assert update_score(0, "Win", 8) == 10
    # Win on attempt 20 → formula gives -110, but clamped to min 10
    assert update_score(0, "Win", 20) == 10
