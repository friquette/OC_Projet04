from datetime import datetime

from utility import Utils
from models.tournament import TimeRule
from controllers.player_manager import player_manager
from controllers.tournament_manager import tournament_manager
from controllers.round_manager import round_manager


class TournamentView:
    def __init__(self):
        self.players = []
        self.rounds = []

        self.utils = Utils()
        self.player_manager = player_manager
        self.round_manager = round_manager

        self.user_choice = None

    def display_tournament_creation(self):
        players = []
        new_player_list = []
        name = self.utils.ask_pattern('Nom: ')
        location = self.utils.ask_pattern('Lieu: ')
        date = self.utils.ask_date('Date (AAAA-MM-JJ HH:MM): ', False)
        print(type(date))
        identifier = f"{location}{date}"[:-9]
        print("Contrôle du temps: ")
        time_rule = self.utils.ask_choices(list(TimeRule))
        description = self.utils.ask_pattern('Description: ')
        nb_round = self.utils.ask_int('Nombre de round: ')

        for i in range(8):
            while True:
                user_id_choice = self.utils.ask_identifier(f"Id du joueur {i + 1}: ")
                id_user = player_manager.find_player_by_id(user_id_choice)
                if id_user is None:
                    print("Ce joueur n'existe pas.")
                    continue
                elif id_user not in players:
                    print(f"ID: {id_user['identifier']}, "
                          f"Nom: {id_user['last_name']}, "
                          f"Prénom: {id_user['first_name']}, "
                          f"Date de naissance: {id_user['birthdate']}, "
                          f"Genre: {id_user['gender']}, "
                          f"Classement: {id_user['rank']} \n")
                    players.append(id_user)
                    new_player_list.append([id_user, .0])
                    break
                else:
                    print("Ce joueur est déjà présent dans ce tournoi. Veuillez entrer un nouveau joueur.")
                    continue

        print("~~Début du tournoi~~")
        self.generate_rounds(new_player_list, nb_round)

        tournament_params = {'identifier': identifier, 'name': name, 'location': location, 'tournament_date': date,
                             'nb_round': nb_round, 'rounds': self.rounds, 'players': players, 'time_rule': time_rule,
                             'description': description}
        tournament_manager.create_tournament(tournament_params)

    def generate_rounds(self, player_list, nb_round):
        for i in range(nb_round):
            start_round = datetime.today().replace(second=0, microsecond=0)
            round_name = f"Round {i+1}"
            new_round = []
            self.round_manager.create_match(player_list, i)
            print("")
            for round in self.round_manager.rounds:
                for player in round:
                    self.round_manager.ask_score(player)
                match = (round[0][:], round[1][:])
                new_round.append(match)
            end_round = datetime.today().replace(second=0, microsecond=0)

            round_params = {'name': round_name, 'start_date': start_round, 'end_date': end_round,
                            'match_list': new_round}
            round_manager.create_round(round_params)
            round_manager.serialize_round()
            self.rounds.append(round_manager.this_round)

    def display_tournaments(self):
        sorted_tournaments = sorted(tournament_manager.tournaments.items(),
                                    key=lambda tournament: tournament[1]['tournament_date'])

        print("Affichage de tous les tournois: ")
        for tournament in sorted_tournaments:
            print(f"Identifiant: {tournament[1]['identifier']}, "
                  f"Nom: {tournament[1]['name']}, "
                  f"Lieu: {tournament[1]['location']}, "
                  f"Date: {tournament[1]['tournament_date'][:-3].replace('T', ' ')}, "
                  f"Nombre de tours: {tournament[1]['nb_round']}, "
                  f"Contrôle du temps: {tournament[1]['time_rule']}, "
                  f"Description: {tournament[1]['description']}")

    def display_tournament_by_id(self):
        self.user_choice = self.utils.ask_tournament_identifier("Entrez l'id d'un tournoi (format:lieuAAAA-MM-JJ): ")
        selected_tournament = tournament_manager.find_tournament_by_id(self.user_choice)

        print(f"Identifiant: {selected_tournament['identifier']}, "
              f"Nom: {selected_tournament['name']}, "
              f"Lieu: {selected_tournament['location']}, "
              f"Date: {selected_tournament['tournament_date'][:-3].replace('T', ' ')}, "
              f"Nombre de tours: {selected_tournament['nb_round']}, "
              f"Contrôle du temps: {selected_tournament['time_rule']}, "
              f"Description: {selected_tournament['description']}")
        print("Rounds: ")
        for round in selected_tournament['rounds']:
            print(f"{round['name']}: ")
            print(f"Début du round: {round['start_date'][:-3].replace('T', ' ')}, "
                  f"Fin du round: {round['end_date'][:-3].replace('T', ' ')}")
            for match in round['match_list']:
                print(f"{match[0][0]['last_name']} {match[0][0]['first_name']} (score: {match[0][1]}) "
                      f"contre "
                      f"{match[1][0]['last_name']} {match[1][0]['first_name']} (score: {match[1][1]}).")
            print("")

    def display_players_in_tournament(self):
        self.user_choice = self.utils.ask_tournament_identifier("Entrez l'id d'un tournoi (format:lieuAAAA-MM-JJ): ")
        selected_tournament = tournament_manager.find_tournament_by_id(self.user_choice)
        sorted_players = sorted(selected_tournament['players'], key=lambda player: (player['last_name'],
                                                                                    player['first_name']))

        for player in sorted_players:
            print(f"ID: {player['identifier']}, "
                  f"Nom: {player['last_name']}, "
                  f"Prenom: {player['first_name']}, "
                  f"Date de naissance: {player['birthdate']}, "
                  f"Genre: {player['gender']}, "
                  f"Classement: {player['rank']}")


tournament_creation = TournamentView()
