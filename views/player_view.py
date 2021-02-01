""" This module contains the view of the player."""
from utility import Utils
from uuid import uuid4

from models.player import Gender
from player_manager import player_manager
from serializable import Serializable


class PlayerView:
    """ Class of the view player.

    Display the creation of a player to the user.

    """
    def __init__(self):
        self.utils = Utils()

        self.player_id = None
        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.gender = None
        self.rank = None
        self.player_params = None

        self.redo_choices = ['Oui', 'Non']
        self.redo = None
        self.user_id_choice = None
        self.user_choice = None

    def display_player_creation(self):
        """ Display the creation player functionality.

        Set the layout of the creation player functionality. Calls the get_player_info function of
        the controller player to display the different steps of the creation.

        """
        print("~~~~~~~~~~Création d'un joueur~~~~~~~~~~")
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
        self.ask_redo_player_creation()

    def ask_redo_player_creation(self):
        print('Voulez-vous créer un nouveau joueur ?')
        self.redo = self.utils.ask_choices(self.redo_choices)

    def display_player_by_id(self):
        self.user_id_choice = self.utils.ask_identifier("Entrez l'id d'un joueur: ")
        print(player_manager.find_player_by_id(self.user_id_choice))
        self.redo = self.utils.ask_choices(self.redo_choices)

    def display_saving(self):
        player_manager.save_player_in_db()

    def display_loading(self):
        player_manager.load_player_from_db()

    def sort_player_by_name(self):
        sort_by_last_name = sorted(player_manager.players.items(), key=lambda player: player[1]['last_name']+player[1]['first_name'])
        print(sort_by_last_name)
        """print(f"ID: {player[1][1]['identifier']}, "
                  f"Nom: {player[1][1]['last_name']}, "
                  f"Prenom: {player[1][1]['first_name']}, "
                  f"Date de naissance: {player[1][1]['birthdate']}, "
                  f"Genre: {player[1][1]['gender']}, "
                  f"Classement: {player[1][1]['rank']}")"""
        
    def sort_player_by_rank(self):
        sort_by_rank = sorted(player_manager.players.items(), key=lambda player: player[1]['rank'])
        print(sort_by_rank)


player_creation = PlayerView()
