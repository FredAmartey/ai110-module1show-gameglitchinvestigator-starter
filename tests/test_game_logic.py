from logic_utils import check_guess, get_range_for_difficulty


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug-fix regression tests ---

def test_hint_direction_when_too_high():
    """Bug: hints were backwards — 'Too High' said 'Go HIGHER!' instead of 'Go LOWER!'"""
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_hint_direction_when_too_low():
    """Bug: hints were backwards — 'Too Low' said 'Go LOWER!' instead of 'Go HIGHER!'"""
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_hard_range_is_larger_than_normal():
    """Bug: Hard mode had a smaller range (1-50) than Normal (1-100)."""
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


def test_check_guess_with_string_secret():
    """Bug: on even attempts the secret was cast to str, causing wrong comparisons."""
    # Passing a string secret should still produce the correct outcome
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"
