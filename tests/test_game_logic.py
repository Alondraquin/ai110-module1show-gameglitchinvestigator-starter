from logic_utils import check_guess, start_new_game, record_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win.
    # check_guess returns (outcome, message), so compare the outcome.
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_new_game_resets_status_to_playing():
    # The original bug: after a win/loss, starting a new game left
    # status as "won"/"lost", so the app refused to let you play again.
    # A new game must always reset status back to "playing".
    state = start_new_game(1, 100)
    assert state["status"] == "playing"


def test_new_game_resets_all_state():
    # A new game should be a clean slate: fresh secret in range, no
    # leftover score, attempts, or history from the previous round.
    state = start_new_game(1, 100)
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["history"] == []
    assert 1 <= state["secret"] <= 100


def test_new_game_secret_respects_difficulty_range():
    # On Easy (1-20) the secret must stay within the given bounds.
    for _ in range(100):
        state = start_new_game(1, 20)
        assert 1 <= state["secret"] <= 20


def test_history_is_not_delayed():
    # The original bug: history lagged one guess behind. record_guess
    # must include the just-submitted value immediately.
    history = []
    history = record_guess(history, 42)
    assert history == [42]

    history = record_guess(history, 7)
    assert history == [42, 7]


def test_record_guess_does_not_mutate_input():
    # record_guess returns a new list so the caller reassigns it,
    # keeping displayed history in sync with the latest guess.
    original = [1, 2]
    result = record_guess(original, 3)
    assert original == [1, 2]
    assert result == [1, 2, 3]
