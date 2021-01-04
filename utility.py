import re
from datetime import date, datetime


def ask_pattern(user_input: str) -> str:
    while True:
        try:
            u_input = input(user_input)
        except ValueError:
            print("Format non valide.")
        else:
            if re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", u_input):
                return u_input
            else:
                print("Format non valide. 2 Caractères minimum. Les chiffres ne sont pas autorisés")


def ask_date(user_input: str) -> date:
    while True:
        try:
            d_input = input(user_input)
        except ValueError:
            print("Format de date non valide.")
        else:
            if re.match(r"^(\d{4})-(\d{2})-(\d{2})$", d_input):
                try:
                    r_date = date.fromisoformat(d_input)
                    return r_date
                except ValueError as error:
                    print("Date non valide:", error)
            elif re.match(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$", d_input):
                try:
                    r_datetime = datetime.fromisoformat(d_input)
                    return r_datetime
                except ValueError as error:
                    print("Date non valide:", error)
            else:
                print("Format de date non valide.")


def ask_choices(choices: list) -> int:
    while True:
        print("Entrez le chiffre de votre choix: ")
        for i, choice in enumerate(choices):
            print("{0} - {1}".format(i+1, choice))
        try:
            user_input = int(input())
        except ValueError:
            print("Veuillez entrer un chiffre.")
        else:
            if 1 <= user_input <= len(choices):
                return user_input
            else:
                print("Cette option n'existe pas.")


def ask_int(user_input: str) -> int:
    while True:
        try:
            r_input = int(input(user_input))
        except ValueError:
            print("Seuls des chiffres sont autorisés.")
        else:
            if r_input < 0:
                print("Veuillez entrer une valeur positive.")
                continue
            else:
                return r_input


def qcm(options: list) -> int:
    while True:
        print("Enter the number of your choice - ")
        for i, option in enumerate(options):
            print(f"{i+1} - {option}")
        try:
            answer = int(input())
        except ValueError:
            print("Not an number !")
        else:
            if 1 <= answer <= len(options):
                return answer
            else:
                print("This option doesn't exist !")
