from utility import name_regex, birthdate_regex
import controlers.c_player as c_player


class Player:
    def __init__(self):
        self.player_last_name = ''
        self.player_first_name = ''
        self.player_birthdate = ''
        self.player_rank = 0

        self.c_player = c_player.ControlPlayer()

    def player_name(self):
        while True:
            self.player_last_name = input("Nom de famille: ")
            if name_regex(self.player_last_name):
                self.c_player.save_last_name(self.player_last_name)
                break
            else:
                print("Format de nom invalide. Doit commencer par une majuscule et contenir au "
                      "moins 2 caractères. Chiffres interdit.")

        while True:
            self.player_first_name = input("Prénom: ")
            if name_regex(self.player_first_name):
                self.c_player.save_first_name(self.player_first_name)
                break
            else:
                print("Format de nom invalide. Doit commencer par une majuscule et contenir au "
                      "moins 2 caractères. Chiffres interdit.")

    def player_birth(self):
        while True:
            self.player_birthdate = input("Date de naissance (JJ-MM-AAAA): ")
            if birthdate_regex(self.player_birthdate):
                self.c_player.save_birthdate(self.player_birthdate)
                break
            else:
                print("Format de date invalide: JJ-MM-AAAA")

    def player_rank_input(self):
        while True:
            try:
                self.player_rank = int(input("Classement: "))
            except ValueError:
                print("Seuls des chiffres sont autorisés.")
            else:
                if self.player_rank < 0:
                    print("Veuillez entrer une valeur positive.")
                    continue
                else:
                    self.c_player.save_rank(self.player_rank)
                    break

    def display_player_info(self):
        r_player = self.c_player.player_info
        print(r_player)
        print("Joueur n°1: {1} {0}, né le {2}. Classement: {3}".format(r_player['last_name'],
                                                                       r_player['first_name'],
                                                                       r_player['birthdate'],
                                                                       r_player['rank']))


def ask_player_info():
    player = Player()
    player.player_name()
    player.player_birth()
    player.player_rank_input()
    player.display_player_info()

