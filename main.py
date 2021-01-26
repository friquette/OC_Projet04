"""Module for testing purposes"""
import utility as utils

import models.tournament as tournament
from player_manager import player_manager
from views.v_player import player_creation
from views.v_menu import MenuView


class Controller:
    def __init__(self):
        self.player_id = None
        self.t_name = None
        self.t_location = None
        self.t_date = None
        self.t_nb_round = None
        self.t_rounds = ['round1']
        self.t_players = None
        self.t_time_rule = None
        self.t_description = None
        self.tournament_params = None

        self.tournament = None
        self.utils = utils.Utils()
        self.menu = MenuView()
        self.player_creation = player_creation

    def get_user_choice(self):
        while True:
            self.menu.display_menu()
            if self.menu.user_choice == self.menu.menu_choices[0]:
                while True:
                    self.player_creation.display_player_creation()
                    if self.player_creation.redo != self.player_creation.redo_choices[0]:
                        print(self.player_creation.players)
                        break
            elif self.menu.user_choice == self.menu.menu_choices[2]:
                while True:
                    self.player_creation.display_player_by_id()
                    if self.player_creation.redo != self.player_creation.redo_choices[0]:
                        break
            else:
                print('fermeture du programme')
                break

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


controller = Controller()
controller.get_user_choice()
"""for i in range(1):
    player_creation.display_player_creation()
print(player_manager.players)
create_player.display_tournament_creation()"""
