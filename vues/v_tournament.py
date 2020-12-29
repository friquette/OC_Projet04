from utility import name_regex, date_regex
import vues.v_player as v_player
import controlers.c_tournament as c_tournament
import controlers.c_player as c_player


class Tournament:
    def __init__(self):
        self.name = ""
        self.location = ""
        self.date = ""
        self.nb_rounds = 4
        self.nb_players = 8
        self.time_control = ''
        self.description = ''

        self.c_tournament = c_tournament.ControlTournament()
        self.v_player = v_player.Player()
        self.c_player = c_player.ControlPlayer()

    def ask_tournament_name(self):
        self.name = input("Nom: ")
        self.c_tournament.save_tournament_name(self.name)

    def ask_tournament_location(self):
        while True:
            self.location = input("Lieu: ")
            if name_regex(self.location):
                self.c_tournament.save_tournament_location(self.location)
                break
            else:
                print("Format de nom invalide. Doit commencer par une majuscule et contenir au "
                      "moins 2 caractères. Chiffres interdit.")

    def ask_tournament_date(self):
        while True:
            self.date = input("Date et heure (JJ-MM-AAAA hh:mm) ")
            if date_regex(self.date):
                self.c_tournament.save_tournament_date(self.date)
                break
            else:
                print("Format de date et d'heure invalide (JJ-MM-AAAA hh:mm): ")

    def ask_tournament_nb_rounds(self):
        while True:
            try:
                self.nb_rounds = int(input("Nombre de tours: "))
            except ValueError:
                print("Veuillez entrer un chiffre.")
            else:
                if self.nb_rounds <= 1:
                    print("Minimum 1 tour requis.")
                    continue
                else:
                    self.c_tournament.save_tournament_nb_rounds(self.nb_rounds)
                    break

    def ask_tournament_nb_players(self):
        while True:
            try:
                self.nb_players = int(input("Nombre de joueurs: "))
            except ValueError:
                print("Veuillez entrer un chiffre.")
            else:
                if self.nb_players < 2:
                    print("Minimum 2 joueurs requis.")
                    continue
                else:
                    self.c_tournament.save_tournament_nb_players(self.nb_players)
                    break

    def ask_tournament_player_info(self):
        """for i in range(self.nb_players):
            print("\n           Création du joueur n°{}".format(i+1))
            self.v_player.ask_p_info()"""
        self.v_player.ask_p_info()

    def ask_tournament_time_control(self):
        print("          Contrôle du temps: ")
        print("1 - Bullet \n"
              "2 - Blitz \n"
              "3 - Coup rapide ")
        while True:
            try:
                self.time_control = int(input("Choisissez un contrôle du temps: "))
            except ValueError:
                print("Veuillez entrer un chiffre entre 1 et 3.")
            else:
                if self.time_control == 1:
                    self.c_tournament.save_tournament_time_control("Bullet")
                    break
                elif self.time_control == 2:
                    self.c_tournament.save_tournament_time_control("Blitz")
                    break
                elif self.time_control == 3:
                    self.c_tournament.save_tournament_time_control("Coup rapide")
                    break
                else:
                    print("Veuillez entrer un chiffre entre 1 et 3.")

    def ask_tournament_decription(self):
        self.description = input("Description: ")
        self.c_tournament.save_tournament_description(self.description)

    def display_tournament_info(self):
        r_tournament = self.c_tournament.tournament_info
        print(r_tournament)

    def ask_tournament_info(self):
        # self.ask_tournament_name()
        # self.ask_tournament_location()
        # self.ask_tournament_date()
        # self.ask_tournament_nb_rounds()
        self.ask_tournament_nb_players()
        for i in range(self.nb_players):
            self.ask_tournament_player_info()
            self.c_tournament.save_tournament_players()

        # self.v_player.display_player_info()
        # self.ask_tournament_time_control()
        # self.ask_tournament_decription()


def display_tournament_creation():
    questions = Tournament()
    questions.ask_tournament_info()
    questions.display_tournament_info()
