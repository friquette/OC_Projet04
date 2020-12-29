import vues.tournament as tm


class Menu:
    def __init__(self):
        self.choice = ""

    def ask_user_choice(self):
        print("          MENU")
        print("1 - Créer un tournoi \n"
              "2 - Mise à jour du classement \n"
              "3 - Rapport \n"
              "4 - Quitter \n")

        while True:
            try:
                self.choice = int(input("Entrez un chiffre pour accéder à la page désirée: "))
                print('')
                self.go_to_page()
            except ValueError:
                print("Vous n'avez pas entré un chiffre")
            else:
                if 1 <= self.choice <= 4:
                    break
                else:
                    print("Cette page n'existe pas")

    def go_to_page(self):
        if self.choice == 1:
            print("          Création d'un tournoi")
            tm.display_tournament_creation()
        elif self.choice == 2:
            print("Mettre à jour le classement")
            # TODO: appeler la fonction qui fera apparaitre la mise à jour du classement
        elif self.choice == 3:
            print("Affichage du rapport")
            # TODO: appeler la fonction qui fera appraitre le rapport
        elif self.choice == 4:
            print("Le programme se ferme")
            # TODO: appeler la fonction qui fermera le programme


def display_menu():
    my_menu = Menu()
    my_menu.ask_user_choice()
