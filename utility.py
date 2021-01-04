import re
from datetime import date, datetime


def ask_pattern(user_input: str) -> str:
    while True:
        try:
            p_input = input(user_input)
        except ValueError:
            print("Format non valide.")
        else:
            if re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", p_input):
                return p_input
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
                    d_date = date.fromisoformat(d_input)
                    return d_date
                except ValueError as error:
                    print("Date non valide:", error)
            elif re.match(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$", d_input):
                try:
                    d_datetime = datetime.fromisoformat(d_input)
                    return d_datetime
                except ValueError as error:
                    print("Date non valide:", error)
            else:
                print("Format de date non valide.")


def ask_choices(choices: list) -> int:
    while True:
        for i, choice in enumerate(choices):
            print("{0} - {1}".format(i+1, choice))
        try:
            c_input = int(input("Entrez le chiffre de votre choix: "))
        except ValueError:
            print("Veuillez entrer un chiffre.")
        else:
            if 1 <= c_input <= len(choices):
                return c_input
            else:
                print("Cette option n'existe pas.\n")


def ask_int(user_input: str) -> int:
    while True:
        try:
            i_input = int(input(user_input))
        except ValueError:
            print("Seuls des chiffres sont autorisés.")
        else:
            if i_input < 0:
                print("Veuillez entrer une valeur positive.")
                continue
            else:
                return i_input
