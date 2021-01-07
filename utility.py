import re
from datetime import date, datetime


class Utils:
    def __init__(self):
        self.u_input = None

    def ask_pattern(self, user_input: str) -> str:
        while True:
            try:
                self.u_input = input(user_input)
            except ValueError:
                print("Format non valide.")
            else:
                if re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", self.u_input):
                    return self.u_input
                else:
                    print("Format non valide. 2 Caractères minimum. Les chiffres ne sont pas autorisés")

    def ask_date(self, user_input: str, choice_date: bool) -> date:
        while True:
            try:
                self.u_input = input(user_input)
            except ValueError:
                print("Format de date non valide.")
            else:
                if re.match(r"^(\d{4})-(\d{2})-(\d{2})$", self.u_input) and choice_date:
                    try:
                        d_date = date.fromisoformat(self.u_input)
                        return d_date
                    except ValueError as error:
                        print("Date non valide:", error)
                elif re.match(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$", self.u_input) and not choice_date:
                    try:
                        d_datetime = datetime.fromisoformat(self.u_input)
                        return d_datetime
                    except ValueError as error:
                        print("Date non valide:", error)
                else:
                    print("Format de date non valide.")

    def ask_choices(self, choices: list) -> int:
        while True:
            for i, choice in enumerate(choices):
                print("{0} - {1}".format(i+1, choice))
            try:
                self.u_input = int(input("Entrez le chiffre de votre choix:"))
            except ValueError:
                print("Veuillez entrer un chiffre.")
            else:
                if 1 <= self.u_input <= len(choices):
                    return self.u_input
                else:
                    print("Cette option n'existe pas.\n")

    def ask_int(self, user_input: str) -> int:
        while True:
            try:
                self.u_input = int(input(user_input))
            except ValueError:
                print("Seuls des chiffres sont autorisés.")
            else:
                if self.u_input < 0:
                    print("Veuillez entrer une valeur positive.")
                    continue
                else:
                    return self.u_input
