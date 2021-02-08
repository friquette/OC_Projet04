"""Module for testing purposes"""
from views.player_view import player_creation
from views.menu_view import MenuView
from views.tournament_view import tournament_creation
from controllers.player_manager import player_manager


class Controller:
    def __init__(self):
        self.menu = MenuView()
        self.player_creation = player_creation
        self.tournament_creation = tournament_creation

    def get_user_choice(self):
        player_manager.load_player_from_db()
        while True:
            self.menu.display_menu()
            if self.menu.user_choice == self.menu.menu_choices[0]:
                while True:
                    self.player_creation.display_player_creation()
                    player_manager.save_player_in_db()
                    if self.player_creation.redo != self.player_creation.redo_choices[0]:
                        break
            elif self.menu.user_choice == self.menu.menu_choices[1]:
                self.tournament_creation.display_tournament_creation()
                print(self.tournament_creation.tournaments)
            elif self.menu.user_choice == self.menu.menu_choices[2]:
                player_creation.sort_player_by_rank()
            else:
                print('fermeture du programme')
                break


controller = Controller()
controller.get_user_choice()
