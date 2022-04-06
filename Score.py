from typing import Dict, Union


class Score:
    def __init__(self, player_one: str, player_two: str):
        self.player_one = player_one
        self.player_two = player_two
        self.score: Dict[str, int] = {
            player_one: 0,
            player_two: 0,
        }

    def add_point(self, player):
        self.score[player] += 1

    def reset_points(self):
        self.score[self.player_one] = 0
        self.score[self.player_two] = 0

    def get_player_score(self, player: str) -> int:
        return self.score[player]

    def get_difference(self) -> int:
        return abs(self.score[self.player_one] - self.score[self.player_two])

    def get_leading_player(self) -> Union[str, None]:
        if self.score[self.player_one] == self.score[self.player_two]:
            return None

        return self.player_one if self.score[self.player_one] > self.score[self.player_two] else self.player_two

    def get_score_formatted(self) -> str:
        return f"{self.score[self.player_one]}-{self.score[self.player_two]}"


class GameScore(Score):
    def __init__(self, player_one: str, player_two: str):
        super().__init__(player_one, player_two)

        self._formatted_game_point: Dict[int, int] = {
            0: 0,
            1: 15,
            2: 30,
            3: 40
        }

    def get_score_formatted(self):
        if self.score[self.player_one] == 0 and self.get_difference() == 0:
            return ""

        if (self.score[self.player_one] >= 3 or self.score[self.player_two] >= 3) and self.get_difference() == 0:
            return "Deuce"

        if (self.score[self.player_one] >= 3 or self.score[self.player_two] >= 3) and self.get_difference() == 1:
            return f"Advantage {self.get_leading_player()}"

        return f"{self._formatted_game_point[self.score[self.player_one]]}-{self._formatted_game_point[self.score[self.player_two]]}"
