from datetime import datetime

from models.round import Round
from utility import Utils


class RoundManager:
    def __init__(self):
        self.set_matches = set()
        self.rounds = []
        # self.round = None
        self.utils = Utils()

    def create_first_round(self, players: list, nb_rounds: int):
        start_date = datetime.now().replace(second=0, microsecond=0)
        current_round = []
        all_rounds = []
        sorted_players = sorted(players, key=lambda player: player['rank'])
        first_half = sorted_players[0:4]
        second_half = sorted_players[4:8]
        print("Round n°1: ")
        for i in range(4):
            match = ([first_half[i], 0], [second_half[i], 0])
            print(f"Match n°{i + 1}: {match[0][0]['last_name']} {match[0][0]['first_name']} "
                  f"contre {match[1][0]['last_name']} {match[1][0]['first_name']}")
            current_round.append(match)
            self.set_matches.add((match[0][0]['identifier'], match[1][0]['identifier']))

        all_rounds.append(current_round)
        self.ask_score(current_round)
        end_date = datetime.now().replace(second=0, microsecond=0)
        round_params = {'name': "Round 1", 'start_date': start_date, 'end_date': end_date,
                        'match_list': current_round}

        this_round = Round(**round_params)
        self.rounds.append(this_round.params)

        if nb_rounds > 1:
            self.create_next_rounds(all_rounds, nb_rounds)

    def create_next_rounds(self, all_rounds: list, nb_rounds: int):
        for r in range(nb_rounds-1):
            start_date = datetime.now().replace(second=0, microsecond=0)
            new_round = []
            players_w = []

            for match in all_rounds[r]:
                for player in match:
                    players_w.append(player)

            sorted_players = sorted(players_w, key=lambda score: (float(score[1]), score[0]['rank']))
            first_half = sorted_players[0:4]
            second_half = sorted_players[4:8]

            print(f"Round n°{r+2}")
            for i in range(4):
                next_player = 0
                match = (first_half.copy()[0], second_half.copy()[0])

                current_match = (match[0][0]['identifier'], match[1][0]['identifier'])
                invert_current_match = (match[1][0]['identifier'], match[0][0]['identifier'])
                if current_match not in self.set_matches and invert_current_match not in self.set_matches:
                    first_half.pop(0)
                    second_half.pop(0)
                elif len(first_half) == 1 and len(second_half) == 1:
                    pass
                else:
                    while True:
                        next_player += 1
                        match = (first_half[0], second_half[next_player])
                        current_match = (match[0][0]['identifier'], match[1][0]['identifier'])
                        if current_match not in self.set_matches:
                            first_half.pop(0)
                            second_half.pop(next_player)
                            break
                        else:
                            continue

                print(f"Match n°{i + 1}: {match[0][0]['last_name']} {match[0][0]['first_name']} "
                      f"contre {match[1][0]['last_name']} {match[1][0]['first_name']}")
                new_round.append(match)
                self.set_matches.add((match[0][0]['identifier'], match[1][0]['identifier']))

            all_rounds.append(new_round)
            self.ask_score(new_round)
            end_date = datetime.now().replace(second=0, microsecond=0)
            round_params = {'name': f"Round {r+2}", 'start_date': start_date, 'end_date': end_date,
                            'match_list': new_round}

            this_round = Round(**round_params)
            self.rounds.append(this_round.params)
            print('')

    def ask_score(self, current_round):
        for matches in current_round:
            for player in matches:
                score = self.utils.ask_float(f"Score de {player[0]['last_name']} {player[0]['first_name']}: ")
                player[1] += float(score)


round_manager = RoundManager()
