""" This module contains the controller of the menu."""
import views.v_player as v_player
import views.v_menu as v_menu


class MenuController:
    """ Class of the controller menu.

    Redirect the user to the correct functionality based on his choice.

    """
    def __init__(self):
        self.v_player = v_player.PlayerView()

    def get_user_choice(self, user_choice):
        """ Get the choice of the user and redirect to the correct functionality based on
        his choice.
        Choice 1 -> calls the display_player_questions function of the view player.
        Choice 2 -> calls the display_ranking function of the 
        Choice 3 -> calls the display_report function of the
        Choice 4 -> calls the quit function.
        Parameter:
        user_choice -- the input of the user in the menu.
        
        """  # TODO: complete the docstring

        if user_choice == 1:
            self.v_player.display_player_questions()
        elif user_choice == 2:
            print("afficher le classement")
        elif user_choice == 3:
            print("afficher le rapport")
        else:
            print("Fermeture du programme")
