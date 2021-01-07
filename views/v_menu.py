import controllers.c_menu as c_menu
import utility as utl


class MenuView:
    def __init__(self):
        # self.c_menu = c_menu.MenuController()
        self.utils = utl.Utils()
        self.menu_choices = ["Créer un tournoi", "Mettre à jour les classements",
                             "Afficher le rapport", "Quitter"]
        self.user_choice = None

    def _display_menu(self):
        print("~~~~~~~~~~~~MENU~~~~~~~~~~~~")
        self.user_choice = self.utils.ask_choices(self.menu_choices)

    def get_user_choice(self):
        # on affiche le menu
        self._display_menu()

        if self.user_choice == 1:
            # on appelle la fonction liée au choix n°1
            print("user_choice: ", self.user_choice)
        elif self.user_choice == 2:
            # on appelle la fonction liée au choix n°2
            print("user_choice: ", self.user_choice)
        elif self.user_choice == 3:
            # on appelle la fonction liée au choix n°3
            print("user_choice: ", self.user_choice)
        else:
            # on appelle la fonction liée au choix n°4
            print("Vous quittez l'application")
