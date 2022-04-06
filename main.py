from typing import Dict


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

    def point_won_by(self, player: str) -> None:
        other_player = self.player_one if player == self.player_two else self.player_two

        self.game_scores[player] += 1

        if self.game_scores[player] >= 4 and self.game_scores[player] + 2 >= self.game_scores[other_player]:

            # reset game score
            self.game_scores[self.player_one] = 0
            self.game_scores[self.player_two] = 0

            # increase winning player's set score
            self.set_scores[player] += 1

    def score(self) -> str:
        player_one_game_score = self.game_scores[self.player_one]
        player_two_game_score = self.game_scores[self.player_two]

        current_game_score_text = ""

        if player_one_game_score == 0 and player_two_game_score == 0:
            current_game_score_text = ""
        elif player_one_game_score >= 3 or player_two_game_score >= 3:
            if player_one_game_score == player_two_game_score:
                current_game_score_text = ", Deuce"
            elif abs(player_one_game_score - player_two_game_score) == 1:
                # the player that's in the lead for this game only - not sets!
                game_winning_player = self.player_one if player_one_game_score > player_two_game_score else self.player_two
                current_game_score_text = f", Advantage {game_winning_player}"
        else:
            current_game_score_text = f", {player_one_game_score * 15}-{player_two_game_score * 15}"

        return f"{self.set_scores[self.player_one]}-{self.set_scores[self.player_two]}{current_game_score_text}"


if __name__ == '__main__':
    match = Match("player 1", "player 2")
    match.point_won_by("player 1")
    match.point_won_by("player 2")

    # this will return "0-0, 15-15"
    assert(match.score() == "0-0, 15-15")
