from utility import Utils
from player_manager import player_manager
from tournament_manager import tournament_manager


class TournamentView:
    def __init__(self):
        self.name = None
        self.location = None
        self.date = None
        self.identifier = None
        self.nb_round = None
        self.players = []
        self.time_rule = None
        self.description = None
        self.rounds = ['round1']
        self.tournament_params = {}
        self.tournaments = None

        self.utils = Utils()
        self.player_manager = player_manager

    def display_tournament_creation(self):
        self.name = self.utils.ask_pattern('Nom: ')
        self.location = self.utils.ask_pattern('Lieu: ')
        self.date = self.utils.ask_date('Date: ', False)
        self.identifier = f"{self.location}{self.date}"[:-9]
        self.nb_round = self.utils.ask_int('Nombre de round: ')
        for i in range(1):
            user_id_choice = self.utils.ask_identifier(f"Id du joueur {i + 1}: ")
            self.players.append(self.player_manager.find_player_by_id(user_id_choice))
        self.time_rule = self.utils.ask_choices(['bullet', 'rapid', 'normal'])
        self.description = self.utils.ask_pattern('Description: ')

        self.tournament_params = {'identifier': self.identifier, 'name': self.name, 'location': self.location,
                                  'tournament_date': self.date, 'nb_round': self.nb_round,
                                  'rounds': self.rounds, 'players': self.players,
                                  'time_rule': self.time_rule, 'description': self.description}
        tournament_manager.create_tournament(self.tournament_params)
        self.tournaments = tournament_manager.tournaments


tournament_creation = TournamentView()
