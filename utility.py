""" This module contains various utility functions."""
import re
from datetime import date, datetime


class Utils:
    """ Class of the utility functions.

    Contains 4 utility functions verifying the user input with regex and return the input if
    the regex is verified. Return an error if not.

    """
    def __init__(self):
        self.u_input = None

    def ask_pattern(self, user_input: str) -> str:
        """ Gets an input and return it if it matches the regex.

        Parameter:
        user_input -- the user input to verify.
        Return:
        u_input -- the user input verified.

        """
        while True:
            self.u_input = input(user_input)
            if re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", self.u_input):
                return self.u_input
            else:
                print("Format non valide. 2 Caractères minimum. Les chiffres ne sont pas autorisés")

    def ask_date(self, user_input: str, choice_date: bool) -> date:
        """ Gets an input and return it if it matches the regex and the bool value.

        If the input matches the regex and the bool value is True, then convert the input in a
        date type. If the input matches the regex and the bool value is False, the convert the
        input in a datetime type.
        Parameter:
        user_input -- the user input to verify.
        choice_date -- choose if the input must be a date (True) or a datetime (False).
        Return:
        d_date -- the user input verified and converted to the date type.
        d_datetime -- the user input verified and converted to the datetime type.

        """
        while True:
            self.u_input = input(user_input)
            if re.match(r"^(\d{4})-(\d{2})-(\d{2})$", self.u_input) and choice_date:
                d_date = date.fromisoformat(self.u_input)
                return d_date
            elif re.match(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$", self.u_input) and not choice_date:
                d_datetime = datetime.fromisoformat(self.u_input)
                return d_datetime
            else:
                print("Format de date non valide.")

    def ask_choices(self, choices: list) -> int:
        """ Gets a list and print all the elements of the list.

        Go through the list and print all the elements one after the other. Then ask the user to
        enter a number within the list range.
        Parameter:
        choices -- the list that will be searched
        Return:
        u_input -- the user input

        """
        while True:
            for i, choice in enumerate(choices):
                print(f"{i+1} - {choice}")
            try:
                self.u_input = int(input("Entrez le chiffre de votre choix:"))
            except ValueError:
                print("Veuillez entrer un chiffre.")
            else:
                if 1 <= self.u_input <= len(choices):
                    return choices[self.u_input-1]
                else:
                    print("Cette option n'existe pas.\n")

    def ask_int(self, user_input: str) -> int:
        """ Gets an input and return it if it is a positive integer.

        Parameter:
        user_input -- the user input to verify.
        Return:
        u_input -- the user input verified and converted into an int.

        """
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

    def ask_identifier(self, user_input: str) -> str:
        while True:
            self.u_input = input(user_input)
            if re.match(r"^[a-z0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}$", self.u_input):
                return self.u_input
            else:
                print("Format non valide.")
