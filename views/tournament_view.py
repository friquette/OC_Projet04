from utility import Utils
from controllers.player_manager import player_manager
from controllers.tournament_manager import tournament_manager
from controllers.round_manager import round_manager


class TournamentView:
    def __init__(self):
        self.players = []
        self.rounds = None

        self.utils = Utils()
        self.player_manager = player_manager
        self.round_manager = round_manager

    def display_tournament_creation(self):
        rounds = []
        new_player_list = []

        # name = self.utils.ask_pattern('Nom: ')
        # location = self.utils.ask_pattern('Lieu: ')
        # date = self.utils.ask_date('Date: ', False)
        # identifier = f"{location}{date}"[:-9]
        # time_rule = self.utils.ask_choices(['bullet', 'rapid', 'normal'])
        # description = self.utils.ask_pattern('Description: ')
        nb_round = self.utils.ask_int('Nombre de round: ')

        """for i in range(8):
            while True:
                user_id_choice = self.utils.ask_identifier(f"Id du joueur {i + 1}: ")
                id_user = self.player_manager.find_player_by_id(user_id_choice)

                if id_user not in self.players:
                    self.players.append(self.player_manager.find_player_by_id(user_id_choice))
                    break
                else:
                    print("Ce joueur est déjà présent dans ce tournoi. Veuillez entrer un nouveau joueur.")
                    continue"""

        players = ["b03017d2-a3a1-406c-af08-88d0be93e356", "11dc9bec-3d10-4312-982f-754a26b475a2",
                   "1c1590f2-1484-4d02-b194-c17a5ffdeb28", "b3df014b-3975-4313-a196-d9760d8b8353",
                   "de5352cf-3fff-4236-a2fc-3b38a2d07748", "d451280e-a734-4936-939f-64034d22d828",
                   "4ed6aa39-d91b-4209-bbb9-e1a83a24140d", "ad39f897-7fad-4217-aefd-bf8243c7c759"]

        for player in players:
            id_user = self.player_manager.find_player_by_id(player)
            new_player_list.append([id_user, 0])

        for i in range(nb_round):
            self.round_manager.create_match(new_player_list, i)
            for new_player in new_player_list:
                self.round_manager.ask_score(new_player)

            rounds.append(self.round_manager.rounds.copy())
            for round in rounds:
                print(f"round: {round} \n")

        tournament_params = {'identifier': "identifier", 'name': "name", 'location': "location",
                             'tournament_date': "2021-02-16 15:02", 'nb_round': nb_round, 'rounds': ['rounds'],
                             'players': self.players, 'time_rule': "time rule", 'description': "description"}
        tournament_manager.create_tournament(tournament_params)


tournament_creation = TournamentView()
