from utility import name_regex, date_regex
from vues.player import ask_player_info


class Tournament:
    def __init__(self):
        self.name = ""
        self.location = ""
        self.date = ""
        self.nb_tours = 4
        self.time_control = ''
        self.description = ''

    def ask_tournament_info(self):
        self.name = input("Nom: ")

        while True:
            self.location = input("Lieu: ")
            if name_regex(self.location):
                # TODO: appeler la fonction qui va enregistrer le lieu saisi par l'utilisateur
                break
            else:
                print("Format de nom invalide. Doit commencer par une majuscule et contenir au "
                      "moins 2 caractères. Chiffres interdit.")

        while True:
            self.date = input("Date et heure: ")
            if date_regex(self.date):
                # TODO: appeler la fonction qui va enregistrer la date et l'heure saisies par l'utilisateur
                break
            else:
                print("Format de date et d'heure invalide: JJ-MM-AAAA HH:MM")

        while True:
            try:
                self.nb_tours = int(input("Nombre de tours: "))
            except ValueError:
                print("Veuillez entrer un chiffre.")
            else:
                if self.nb_tours <= 1:
                    print("Minimum 1 tour requis")
                    continue
                else:
                    # TODO: appeler la fonction qui va enregistrer le nombre de tours saisi par l'utilisateur
                    break

        print("          Création d'un joueur          ")
        ask_player_info()

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

        self.description = input("Description: ")
        # TODO: appeler la fonction qui va enregistrer la description saisie par l'utilisateur


def display_tournament_creation():
    questions = Tournament()
    questions.ask_tournament_info()
