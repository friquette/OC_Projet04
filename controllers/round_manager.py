from models.round import Round


class RoundManager:
    def __init__(self):
        self.set_matches = set()
        self.rounds = []
        self.round = None

    def create_first_round(self, players: list, nb_rounds: int):
        current_round = []
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

        self.rounds.append(current_round)
        self.ask_score(current_round)
        round_params = {'name': "Round 1", 'start_date': "2021-02-11 16:18", 'end_date': "2021-02-11 16:20",
                        'match_list': current_round}
        if nb_rounds > 1:
            self.create_next_rounds(nb_rounds)
        else:
            self.create_round(round_params)

    def create_next_rounds(self, nb_rounds: int):
        for r in range(nb_rounds-1):
            my_round = []
            players_w = []

            for match in self.rounds[r]:
                for player in match:
                    players_w.append(player)

            sorted_players = sorted(players_w, key=lambda score: (float(score[1]), float(score[0]['rank'])))
            first_half = sorted_players[0:4]
            second_half = sorted_players[4:8]

            print(f"Round n°{r+2}")
            for i in range(4):
                next_player = 0
                match = (first_half[0], second_half[0])
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
                my_round.append(match)
                self.set_matches.add((match[0][0]['identifier'], match[1][0]['identifier']))

            self.rounds.append(my_round)
            self.ask_score(my_round)

    def ask_score(self, current_round):
        for matches in current_round:
            for player in matches:
                score = input(f"Score de {player[0]['last_name']} {player[0]['first_name']}: ")
                player[1] += float(score)

    def create_round(self, params):
        self.round = Round(**params)
        self.round[self.round.name] = self.round.params


round_manager = RoundManager()
