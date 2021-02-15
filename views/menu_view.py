""" This module contains the view of the menu."""
import utility as utl


class MenuView:
    """ Class of the view menu.

    Create a list of choices which will be used to print the different possibilities to
    the user and ask him to choose.

    """
    def __init__(self):
        self.utils = utl.Utils()
        self.menu_choices = ["Créer un joueur", "Créer un tournoi", "Rapport", "Quitter"]
        self.rapport_choices = ["Afficher tous les joueurs", "Afficher les joueurs d'un tournoi",
                        "Afficher tous les tournois", "Afficher les tours d'un tournoi",
                        "Afficher les matchs d'un tournoi"]
        self.sort_choices = ["Trier par ordre alphabétique", "Trier par classement"]
        self.user_choice = None

    def display_menu(self):
        """ Display the menu.

        Set the layout of the menu. Print the menu and calls the get_user_choice function of the
        controller menu to redirect the user.

        """
        print("~~~~~~~~~~~~MENU~~~~~~~~~~~~")
        self.user_choice = self.utils.ask_choices(self.menu_choices)
        print("")

    def display_sort_choice(self):
        print("Affichage de tous les joueurs: ")
        self.user_choice = self.utils.ask_choices(self.sort_choices)
        print("")

    def display_report_choice(self):
        print("Affichage des rapports: ")
        self.user_choice = self.utils.ask_choices(self.rapport_choices)
        print("")
