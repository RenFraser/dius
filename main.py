from typing import Dict, Union


def format_game_point(points: int) -> Union[int, None]:
    formatted_points = {
        0: 0,
        1: 15,
        2: 30,
        3: 40
    }

    return formatted_points.get(points, None)


class Match:
    def __init__(self, player_one: str, player_two: str) -> None:
        self.player_one = player_one
        self.player_two = player_two

        self.game_scores: Dict[str, int] = {
            player_one: 0,
            player_two: 0,
        }

        self.set_scores: Dict[str, int] = {
            player_one: 0,
            player_two: 0,
        }

    def _are_game_points_equal(self) -> bool:
        return self.game_scores[self.player_one] == self.game_scores[self.player_two]

    def _is_deuce(self) -> bool:
        return (self.game_scores[self.player_one] >= 3 or self.game_scores[self.player_two] >= 3) and self._are_game_points_equal()

    def _get_game_score_difference(self) -> int:
        return abs(self.game_scores[self.player_one] - self.game_scores[self.player_two])

    def _get_set_score(self) -> str:
        return f"{self.set_scores[self.player_one]}-{self.set_scores[self.player_two]}"

    def point_won_by(self, player: str):
        opponent = self.player_one if player == self.player_two else self.player_two

        self.game_scores[player] += 1

        if self.game_scores[player] >= 4 and self.game_scores[player] >= self.game_scores[opponent] + 2:

            # reset game score
            self.game_scores[self.player_one] = 0
            self.game_scores[self.player_two] = 0

            # increase winning player's set score
            self.set_scores[player] += 1

    # *leading* and not winning to avoid confusion about whether a player has won
    # returns None if both players have an equal score
    def _get_game_leading_player(self) -> Union[str, None]:
        if self._are_game_points_equal():
            return None

        return self.player_one if self.game_scores[self.player_one] > self.game_scores[self.player_two] else self.player_two

    def score(self) -> str:
        if self.game_scores[self.player_one] == 0 and self._are_game_points_equal():
            return self._get_set_score()

        if self._is_deuce():
            return f"{self._get_set_score()}, Deuce"

        if (self.game_scores[self.player_one] >= 3 or self.game_scores[self.player_two] >= 3) and self._get_game_score_difference() == 1:
            return f"{self._get_set_score()}, Advantage {self._get_game_leading_player()}"

        return f"{self._get_set_score()}, {format_game_point(self.game_scores[self.player_one])}-{format_game_point(self.game_scores[self.player_two])}"


# #TODO: add sets winning critea - I've mised it

if __name__ == '__main__':
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")

    # this will return "0-0, 15-15"
    assert(match.score() == "0-0, 15-15")
