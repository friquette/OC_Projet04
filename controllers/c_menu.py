import utility as utl
import views.v_menu as v_menu


class MenuController:
    def __init__(self):
        self.menu_choices = ["Créer un tournoi", "Mettre à jour les classements",
                             "Afficher le rapport", "Quitter"]
        self.utils = utl.Utils()
        self.menu = v_menu.MenuView()
        self.user_choice = None

    # créer la liste des choix possibles
    def choices(self):
        self.user_choice = self.utils.ask_choices(self.menu_choices)
        self.menu.get_user_choice(self.user_choice)

    # récupérer le choix de l'utilisateur
    def get_user_choice(self):
        pass
