from models.round import Round
from utility import Utils


class RoundManager:
    def __init__(self):
        self.set_matches = set()
        self.this_round = {}
        self.current_round = None
        self.rounds = []
        self.utils = Utils()

    def create_match(self, players_list, nb_round):
        print("")
        print(f"Round n°{nb_round+1}")
        self.rounds.clear()

        sorted_players = sorted(players_list, key=lambda player: (player[1], player[0]['rank'], player[0]['last_name']))
        first_half = sorted_players[0:4]
        second_half = sorted_players[4:8]

        for i in range(4):
            next_player = 0
            match = (first_half[0], second_half[0])

            current_match = (match[0][0]['identifier'], match[1][0]['identifier'])
            inverted_current_match = current_match[::-1]

            if current_match not in self.set_matches and inverted_current_match not in self.set_matches:
                print(f"{match[0][0]['last_name']} {match[0][0]['first_name']} contre "
                      f"{match[1][0]['first_name']} {match[1][0]['last_name']}")
                first_half.pop(0)
                second_half.pop(0)
            elif len(first_half) == 1 and len(second_half) == 1:
                pass
            else:
                while True:
                    next_player += 1
                    match = (first_half[0], second_half[next_player])

                    current_match = (match[0][0]['identifier'], match[1][0]['identifier'])
                    inverted_current_match = current_match[::-1]

                    if current_match not in self.set_matches and inverted_current_match not in self.set_matches:
                        print(f"{match[0][0]['last_name']} {match[0][0]['first_name']} contre "
                              f"{match[1][0]['first_name']} {match[1][0]['last_name']}")
                        first_half.pop(0)
                        second_half.pop(next_player)
                        break
                    else:
                        continue

            self.set_matches.add(current_match)
            self.rounds.append(match)

    def ask_score(self, players_list):
        new_score = self.utils.ask_float(f"Score de {players_list[0]['last_name']} {players_list[0]['first_name']}: ")
        players_list[1] += float(new_score)

    def create_round(self, params):
        self.current_round = Round(**params)
        self.this_round = self.current_round.params

    def serialize_round(self):
        self.current_round.serialize()


round_manager = RoundManager()
