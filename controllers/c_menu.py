import views.v_player as v_player
import views.v_menu as v_menu


class MenuController:
    def __init__(self):
        self.v_player = v_player.PlayerView()

    def redirect_to_player_creation(self):
        self.v_player.display_player_questions()

    def get_user_choice(self, user_choice):
        if user_choice == 1:
            self.v_player.display_player_questions()
        elif user_choice == 2:
            print("afficher le classement")
        elif user_choice == 3:
            print("afficher le rapport")
        else:
            print("Fermeture du programme")
