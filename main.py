"""Main module"""
from views.menu_view import menu_creation
from views.tournament_view import tournament_creation
from controllers.tournament_manager import tournament_manager
from views.player_view import player_creation
from controllers.player_manager import player_manager


class Controller:
    """ Class of the general controller

    Load all the players and the tournaments from the database at the opening of the software.
    This class controls the menu. It saves each player and each tournament in the database at
    the end of their creation.

    """
    def get_user_choice(self):
        player_manager.load_player_from_db()
        tournament_manager.load_tournament_from_db()
        while True:
            menu_creation.display_menu()

            if menu_creation.user_choice == menu_creation.menu_choices[0]:
                while True:
                    player_creation.display_player_creation()
                    player_manager.save_player_in_db()
                    if player_creation.redo != player_creation.redo_choices[0]:
                        break

            elif menu_creation.user_choice == menu_creation.menu_choices[1]:
                tournament_creation.display_tournament_creation()
                tournament_manager.save_tournament_in_db()

            elif menu_creation.user_choice == menu_creation.menu_choices[2]:
                menu_creation.display_report_choice()

                if menu_creation.user_choice == menu_creation.report_choices[0]:
                    menu_creation.display_players_choice()

                    if menu_creation.user_choice == menu_creation.players_choices[0]:
                        menu_creation.display_sort_choice()

                        if menu_creation.user_choice == menu_creation.sort_choices[0]:
                            player_creation.sort_player_by_name()
                        else:
                            player_creation.sort_player_by_rank()
                    else:
                        tournament_creation.display_players_in_tournament()

                else:
                    menu_creation.display_tournament_choices()

                    if menu_creation.user_choice == menu_creation.tournament_choices[0]:
                        tournament_creation.display_tournaments()
                    else:
                        tournament_creation.display_tournament_by_id()

            else:
                print('Fermeture du programme.')
                break


if __name__ == "__main__":
    controller = Controller()
    controller.get_user_choice()
