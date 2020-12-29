from utility import name_regex, date_regex
from vues.player import ask_player_info


class Tournament:
    def __init__(self):
        self.name = ""
        self.location = ""
        self.date = ""
        self.nb_rounds = 4
        self.nb_players = 8
        self.time_control = ''
        self.description = ''

    def ask_tournament_name(self):
        self.name = input("Nom: ")

    def ask_tournament_location(self):
        while True:
            self.location = input("Lieu: ")
            if name_regex(self.location):
                # TODO: appeler la fonction qui va enregistrer le lieu saisi par l'utilisateur
                break
            else:
                print("Format de nom invalide. Doit commencer par une majuscule et contenir au "
                      "moins 2 caractères. Chiffres interdit.")

    def ask_tournament_date(self):
        while True:
            self.date = input("Date et heure (JJ-MM-AAAA hh:mm) ")
            if date_regex(self.date):
                # TODO: appeler la fonction qui va enregistrer la date et l'heure saisies par l'utilisateur
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
                    # TODO: appeler la fonction qui va enregistrer le nombre de tours saisi par l'utilisateur
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
                    # TODO: appeler la fonction qui va enregistrer le nombre de joueurs saisi par l'utilisateur
                    break

    def ask_tournament_player_info(self):
        for i in range(self.nb_players):
            print("\n           Création du joueur n°{}".format(i+1))
            ask_player_info()

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
                    # TODO: appeler la fonction qui va enregistrer le choix de l'utilisateur
                    break
                elif self.time_control == 2:
                    # TODO: appeler la fonction qui va enregistrer le choix de l'utilisateur
                    break
                elif self.time_control == 3:
                    # TODO: appeler la fonction qui va enregistrer le choix de l'utilisateur
                    break
                else:
                    print("Veuillez entrer un chiffre entre 1 et 3.")

    def ask_tournament_decription(self):
        self.description = input("Description: ")
        # TODO: appeler la fonction qui va enregistrer la description saisie par l'utilisateur

    def ask_tournament_info(self):
        self.ask_tournament_name()
        self.ask_tournament_location()
        self.ask_tournament_date()
        self.ask_tournament_nb_rounds()
        self.ask_tournament_nb_players()
        self.ask_tournament_player_info()
        self.ask_tournament_time_control()
        self.ask_tournament_decription()


def display_tournament_creation():
    questions = Tournament()
    questions.ask_tournament_info()