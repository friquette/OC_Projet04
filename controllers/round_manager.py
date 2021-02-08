

class RoundManager:
    def __init__(self):
        self.player = []
        self.match = None
        self.current_round = []

    def create_first_round(self, players: list):
        sorted_players = sorted(players, key=lambda player: player['rank'])
        first_half = sorted_players[0:4]
        second_half = sorted_players[4:8]
        for i in range(4):
            self.match = ([first_half[i], 0], [second_half[i], 0])
            self.current_round.append(self.match)
            print(self.match)


round_manager = RoundManager()
