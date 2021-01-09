""" This module contains the view of the menu."""
import controllers.c_menu as c_menu
import utility as utl


class MenuView:
    """ Class of the view menu.

    Create a list of choices which will be used to print the different possibilities to
    the user and ask him to choose.

    """
    def __init__(self):
        self.utils = utl.Utils()
        self.menu_choices = ["Créer un tournoi", "Mettre à jour les classements",
                             "Afficher le rapport", "Quitter"]
        self.user_choice = None
        self.c_menu = c_menu.MenuController()

    def display_menu(self):
        """ Display the menu.

        Set the layout of the menu. Print the menu and calls the get_user_choice function of the
        controller menu to redirect the user.

        """
        print("~~~~~~~~~~~~MENU~~~~~~~~~~~~")
        self.user_choice = self.utils.ask_choices(self.menu_choices)
        print("")
        self.c_menu.get_user_choice(self.user_choice)
