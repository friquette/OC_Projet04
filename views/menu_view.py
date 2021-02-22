""" This module contains the view of the menu."""
from misc import utility as utl


class MenuView:
    """ Class of the view menu.

    Create a list of choices which will be used to print the different possibilities to
    the user and ask him to choose. It contains 5 methods:
    display_menu: displays the menu choices (créer un joueur, créer un tournoi, rapport, quitter).
    display_report_choices: displays the report choices (joueurs, tournois).
    display_players_choices: displays the players choices (afficher tous les joueurs, afficher les
                    joueurs d'un tournoi).
    display_sort_choice: displays the choices to sort the players (par ordre alphabétique, par classement).
    display_tournament_choices: displays the tournaments choices (afficher tous les tournois, afficher
                    les détails d'un tournoi).

    """
    def __init__(self):
        self.utils = utl.Utils()
        self.menu_choices = ["Créer un joueur", "Créer un tournoi", "Modifier le classement d'un joueur",
                             "Rapport", "Quitter"]
        self.report_choices = ["Joueurs", "Tournois"]
        self.players_choices = ["Afficher tous les joueurs", "Afficher les joueurs d'un tournoi"]
        self.tournament_choices = ["Afficher tous les tournois", "Afficher les détails d'un tournoi"]
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

    def display_report_choice(self):
        print("Choisissez une catégorie: ")
        self.user_choice = self.utils.ask_choices(self.report_choices)
        print("")

    def display_players_choice(self):
        print("Choisissez un rapport: ")
        self.user_choice = self.utils.ask_choices(self.players_choices)
        print("")

    def display_sort_choice(self):
        print("Affichage de tous les joueurs: ")
        self.user_choice = self.utils.ask_choices(self.sort_choices)
        print("")

    def display_tournament_choices(self):
        print("Choisissez un rapport: ")
        self.user_choice = self.utils.ask_choices(self.tournament_choices)
        print("")


menu_creation = MenuView()
