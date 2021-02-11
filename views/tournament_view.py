from utility import Utils
from controllers.player_manager import player_manager
from controllers.tournament_manager import tournament_manager
from controllers.round_manager import round_manager


class TournamentView:
    def __init__(self):
        self.players = []
        self.rounds = ['round1']

        self.utils = Utils()
        self.player_manager = player_manager
        self.round_manager = round_manager

    def display_tournament_creation(self):
        # name = self.utils.ask_pattern('Nom: ')
        # location = self.utils.ask_pattern('Lieu: ')
        # date = self.utils.ask_date('Date: ', False)
        # identifier = f"{location}{date}"[:-9]
        nb_round = self.utils.ask_int('Nombre de round: ')
        for i in range(8):
            while True:
                user_id_choice = self.utils.ask_identifier(f"Id du joueur {i + 1}: ")
                id_user = self.player_manager.find_player_by_id(user_id_choice)

                if id_user not in self.players:
                    self.players.append(self.player_manager.find_player_by_id(user_id_choice))
                    break
                else:
                    print("Ce joueur est déjà présent dans ce tournoi. Veuillez entrer un nouveau joueur.")
                    continue
        # time_rule = self.utils.ask_choices(['bullet', 'rapid', 'normal'])
        # description = self.utils.ask_pattern('Description: ')

        self.round_manager.create_first_round(self.players, nb_round)
        print(self.round_manager.round.params)

        """tournament_params = {'identifier': identifier, 'name': name, 'location': location,
                             'tournament_date': date, 'nb_round': nb_round, 'rounds': self.rounds,
                             'players': self.players, 'time_rule': time_rule, 'description': description}
        tournament_manager.create_tournament(tournament_params)"""


tournament_creation = TournamentView()
