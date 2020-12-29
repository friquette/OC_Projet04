from utility import name_regex, birthdate_regex


class Player:
    def __init__(self):
        self.player_last_name = ''
        self.player_first_name = ''
        self.player_birthdate = ''
        self.player_rank = 0

    def player_name(self):
        while True:
            self.player_last_name = input("Nom de famille: ")
            if name_regex(self.player_last_name):
                break
            else:
                print("Format de nom invalide. Doit commencer par une majuscule et contenir au "
                      "moins 2 caractères. Chiffres interdit.")

        while True:
            self.player_first_name = input("Prénom: ")
            if name_regex(self.player_first_name):
                break
            else:
                print("Format de nom invalide. Doit commencer par une majuscule et contenir au "
                      "moins 2 caractères. Chiffres interdit.")

    def player_birth(self):
        while True:
            self.player_birthdate = input("Date de naissance (JJ-MM-AAAA): ")
            if birthdate_regex(self.player_birthdate):
                break
            else:
                print("Format de date invalide: JJ-MM-AAAA")

    def player_rank_input(self):
        while True:
            try:
                self.player_rank = int(input("Classement: "))
                if self.player_rank < 0:
                    print("Veuillez entrer une valeur positive.")
                    continue
                return self.player_rank
            except ValueError:
                print("Seuls des chiffres sont autorisés.")


def ask_player_info():
    player = Player()
    player.player_name()
    player.player_birth()
    player.player_rank_input()
