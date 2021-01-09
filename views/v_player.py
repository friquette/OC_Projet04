""" This module contains the view of the player."""
import controllers.c_player as c_player


class PlayerView:
    """ Class of the view player.

    Display the creation of a player to the user.

    """
    def __init__(self):
        self.c_player = c_player.PlayerController()

    def display_player_questions(self):
        """ Display the creation player functionality.

        Set the layout of the creation player functionality. Calls the get_player_info function of
        the controller player to display the different steps of the creation.

        """
        print("~~~~~~~~~~Création d'un joueur~~~~~~~~~~")
        self.c_player.get_player_info()
        print("Joueur: {} {}, né le {}. Classement: {}".format(self.c_player.first_name,
                                                               self.c_player.last_name,
                                                               self.c_player.birthdate,
                                                               self.c_player.rank))
