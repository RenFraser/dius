
from Score import GameScore, Score


class Match:
    def __init__(self, player_one: str, player_two: str) -> None:
        self.player_one = player_one
        self.player_two = player_two

        self.game_scores: GameScore = GameScore(self.player_one, self.player_two)
        self.set_scores: Score = Score(self.player_one, self.player_two)

        self.match_ended = False

    def _has_set_been_won(self) -> bool:
        leader = self.set_scores.get_leading_player()

        if not leader:
            return False

        opponent = self.player_one if leader == self.player_two else self.player_two

        leader_score = self.set_scores.get_player_score(leader)
        opponent_score = self.set_scores.get_player_score(opponent)

        return (leader_score >= 6 and opponent_score <= leader_score - 2) or (leader_score == 7 and opponent_score == 6)

    def point_won_by(self, player: str):
        if self.match_ended:
            return

        opponent = self.player_one if player == self.player_two else self.player_two

        self.game_scores.add_point(player)

        player_game_score = self.game_scores.get_player_score(player)
        opponent_game_score = self.game_scores.get_player_score(opponent)

        if player_game_score >= 4 and player_game_score >= opponent_game_score + 2:
            self.game_scores.reset_points()
            self.set_scores.add_point(player)

        if self._has_set_been_won():
            self.match_ended = True

    def score(self) -> str:
        if self.game_scores.get_player_score(self.player_one) == 0 and self.game_scores.get_difference() == 0:
            return self.set_scores.get_score_formatted()

        return f"{self.set_scores.get_score_formatted()}, {self.game_scores.get_score_formatted()}"


if __name__ == '__main__':
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")

    # this will return "0-0, 15-15"
    assert(match.score() == "0-0, 15-15")
