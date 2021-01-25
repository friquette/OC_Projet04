"""Module for testing purposes"""
import utility as utils
from uuid import uuid4

import models.tournament as tournament
from player_manager import player_manager
from models.player import Gender, Player


class CreatePlayer:
    def __init__(self):
        self.player_id = None
        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.gender = None
        self.rank = None
        self.player_params = None

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
        self.player_id = uuid4()
        self.last_name = self.utils.ask_pattern('Nom: ')
        self.first_name = self.utils.ask_pattern('Prénom: ')
        self.birthdate = self.utils.ask_date('Date de naissance: ', True)
        print("Genre: ")
        self.gender = self.utils.ask_choices(list(Gender))
        self.rank = self.utils.ask_int('Classement: ')
        self.player_params = {'identifier': self.player_id, 'last_name': self.last_name, 'first_name': self.first_name,
                              'birthdate': self.birthdate, 'gender': self.gender, 'rank': self.rank}

        player_manager.create_player(self.player_params)

    def display_tournament_creation(self):
        self.t_name = self.utils.ask_pattern('Nom: ')
        self.t_location = self.utils.ask_pattern('Lieu: ')
        self.t_date = self.utils.ask_date('Date: ', False)
        self.t_nb_round = self.utils.ask_int('Nombre de round: ')
        self.t_time_rule = self.utils.ask_choices(['bullet', 'rapid', 'normal'])
        self.t_description = self.utils.ask_pattern('Description: ')
        for i in range(8):
            # TODO: demander les id des players jusqu'à ce qu'il y en ai 8 de valide
            pass

        self.tournament_params = {'name': self.t_name, 'location': self.t_location, 'tournament_date': self.t_date,
                                  'nb_round': self.t_nb_round, 'rounds': self.t_rounds, 'players': self.t_players,
                                  'time_rule': self.t_time_rule, 'description': self.t_description}
        self.tournament = tournament.Tournament(**self.tournament_params)
        self.tournament.serialize()
        print(self.tournament.params)


create_player = CreatePlayer()
for i in range(1):
    create_player.display_player_creation()
print(player_manager.players)
# create_player.display_tournament_creation()
