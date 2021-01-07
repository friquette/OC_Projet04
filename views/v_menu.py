import controllers.c_menu as c_menu
import utility as utl


class MenuView:
    def __init__(self):
        self.utils = utl.Utils()
        self.menu_choices = ["Créer un tournoi", "Mettre à jour les classements",
                             "Afficher le rapport", "Quitter"]
        self.user_choice = None
        self.c_menu = c_menu.MenuController()

    def display_menu(self):
        print("~~~~~~~~~~~~MENU~~~~~~~~~~~~")
        self.user_choice = self.utils.ask_choices(self.menu_choices)
        print("")
        self.c_menu.get_user_choice(self.user_choice)
