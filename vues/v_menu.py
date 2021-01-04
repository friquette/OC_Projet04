import utility as utl


def menu():
    print("        MENU")
    choices = ["Créer un tournoi", "Créer un joueur", "Rapport"]
    utl.ask_choices(choices)
