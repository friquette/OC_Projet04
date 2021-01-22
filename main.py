"""Module for testing purposes"""
import utility as utils
from uuid import uuid4

import models.player as player
import models.tournament as tournament
from player_manager import PlayerManager


class CreatePlayer:
    def __init__(self):
        self.player_id = None
        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.gender = None
        self.rank = None
        self.player_params = None
        self.players = {}
        self.player_manager = None

        self.t_name = None
        self.t_location = None
        self.t_date = None
        self.t_nb_round = None
        self.t_rounds = ['round1']
        self.t_players = None
        self.t_time_rule = None
        self.t_description = None
        self.tournament_params = None

        self.player = None
        self.tournament = None
        self.utils = utils.Utils()

    def display_player_creation(self):
        for i in range(2):
            self.player_id = str(uuid4())
            self.last_name = self.utils.ask_pattern('Nom: ')
            self.first_name = self.utils.ask_pattern('Prénom: ')
            self.birthdate = self.utils.ask_date('Date de naissance: ', True)
            print("Genre: ")
            self.gender = self.utils.ask_choices(['Homme', 'Femme'])
            self.rank = self.utils.ask_int('Classement: ')
            self.player_params = {'last_name': self.last_name, 'first_name': self.first_name,
                                  'birthdate': self.birthdate, 'gender': self.gender, 'rank': self.rank}

            self.player = player.Player(**self.player_params)
            self.player.serialize()

            self.player_manager = PlayerManager(self.players, self.player_id, self.player.params)
            self.player_manager.player_verification()
            self.player_id = self.player_manager.id_verification()
            self.players[self.player_id] = self.player.params

    def display_tournament_creation(self):
        self.t_name = self.utils.ask_pattern('Nom: ')
        self.t_location = self.utils.ask_pattern('Lieu: ')
        self.t_date = self.utils.ask_date('Date: ', False)
        self.t_nb_round = self.utils.ask_int('Nombre de round: ')
        self.t_time_rule = self.utils.ask_choices(['bullet', 'rapid', 'normal'])
        self.t_description = self.utils.ask_pattern('Description: ')

        self.t_players = [self.players]

        self.tournament_params = {'name': self.t_name, 'location': self.t_location, 'tournament_date': self.t_date,
                                  'nb_round': self.t_nb_round, 'rounds': self.t_rounds, 'players': self.t_players,
                                  'time_rule': self.t_time_rule, 'description': self.t_description}
        self.tournament = tournament.Tournament(**self.tournament_params)
        self.tournament.serialize()
        print(self.tournament.params)


create_player = CreatePlayer()
create_player.display_player_creation()
print(create_player.players)
create_player.display_tournament_creation()
