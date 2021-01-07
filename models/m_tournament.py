import re
from typing import Union
from datetime import datetime


class TournamentModel:
    def __init__(self, name: str, location: str, date: Union[str, datetime], nb_round: int,
                 rounds: list, players: list, time_rule: str, description: str):
        incorrect_values = set()

        try:
            self.name = name
        except ValueError:
            incorrect_values.add("nom")

        try:
            self.location = location
        except ValueError:
            incorrect_values.add("lieu")

        try:
            self.date = date
        except ValueError:
            incorrect_values.add("date")

        try:
            self.nb_round = nb_round
        except ValueError:
            incorrect_values.add("nombre de tours")

        try:
            self.rounds = rounds
        except ValueError:
            incorrect_values.add("liste des instanes rondes")

        try:
            self.players = players
        except ValueError:
            incorrect_values.add("liste des instances de joueur")

        try:
            self.time_rule = time_rule
        except ValueError:
            incorrect_values.add("contrôle du temps")

        try:
            self.description = description
        except ValueError:
            incorrect_values.add("description")

        if incorrect_values:
            raise ValueError(f"Paramètres de model tournoi incorrects: {incorrect_values}")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", value):
            self.__name = value
        else:
            raise ValueError()

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", value):
            self.__location = value
        else:
            raise ValueError()
