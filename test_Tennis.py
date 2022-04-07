from main import Match


def test_NoSetWinsEvenScore():
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")

    assert(match.score() == "0-0, 15-15")


def test_NoSetWinsPlayerOneWinningGame():
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 1")

    assert match.score() == "0-0, 40-15"


def test_NoSetWinsDeuce():
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    match.point_won_by("player 2")

    assert match.score() == "0-0, Deuce"


def test_NoSetWinsAdvantagePlayerOne():
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    match.point_won_by("player 2")
    match.point_won_by("player 1")

    assert match.score() == "0-0, Advantage player 1"


def test_SetWinPlayerOne():
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 1")
    match.point_won_by("player 2")
    match.point_won_by("player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 1")

    assert match.score() == "1-0"


def test_matchWinPlayerOne():
    match = Match("player 1", "player 2")

    num_games_to_win_set = 4
    num_sets_to_win_match = 6

    for i in range(num_sets_to_win_match * num_games_to_win_set):
        match.point_won_by("player 1")

    assert match.score() == "6-0"


def test_matchCannotContinueAfterWin():
    match = Match("player 1", "player 2")

    num_games_to_win_set = 4
    num_sets_to_win_match = 6

    for i in range((num_sets_to_win_match * num_games_to_win_set) + 1):
        match.point_won_by("player 1")

    assert match.score() == "6-0"
