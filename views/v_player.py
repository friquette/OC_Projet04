""" This module contains the view of the player."""
import controllers.c_player as c_player
import utility as utls


class PlayerView:
    """ Class of the view player.

    Display the creation of a player to the user.

    """
    def __init__(self):
        self.c_player = c_player.PlayerController()
        self.utils = utls.Utils()

        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.rank = None

    def display_player_questions(self):
        """ Display the creation player functionality.

        Set the layout of the creation player functionality. Calls the get_player_info function of
        the controller player to display the different steps of the creation.

        """
        print("~~~~~~~~~~Création d'un joueur~~~~~~~~~~")
        self.last_name = self.utils.ask_pattern("Nom: ")
        self.first_name = self.utils.ask_pattern("Prenom: ")
        self.birthdate = self.utils.ask_date("Date de naissance (AAAA-MM-JJ): ", True)
        self.rank = self.utils.ask_int("Classement: ")

        print(f"""Joueur: {self.last_name} {self.first_name}, né le {self.birthdate}.
              Classement: {self.rank}""")
