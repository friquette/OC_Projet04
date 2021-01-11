""" This module contains the model of a tournament."""
import re
from typing import Union
from datetime import datetime


class TournamentModel:
    """ Class of a model player

    Initiate various private variables and store information with a setter to protect the access
    to these variables.
    Parameters:
    name -- the name of the tournament. Type str.
    location -- the location of the tournament. Type str.
    tournament_date -- the date the tournament takes place. Type str or datetime
    nb_round -- the tournament number of rounds. Type int.
    rounds -- list of the instances of the rounds. Type list.
    players -- list of players in the tournament. Type list.
    time_rule -- rule of the tournament time control (bullet, blitz, fast move). Type str.
    description -- description of the tournament. Type str.

    """
    def __init__(self, name: str, location: str, tournament_date: Union[str, datetime], nb_round: int,
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
            self.tournament_date = tournament_date
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

    @property
    def tournament_date(self) -> str:
        return self.__tournament_date

    @tournament_date.setter
    def tournament_date(self, value: Union[str, datetime]):
        if type(value) == str and re.match(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$", value):
            datetime.fromisoformat(value)
            self.__tournament_date = value
        elif type(value) == datetime:
            self.__tournament_date = value
        else:
            raise ValueError()

    @property
    def nb_round(self) -> int:
        return self.__nb_round

    @nb_round.setter
    def nb_round(self, value: int):
        if type(value) == int:
            self.__nb_round = value
        else:
            raise ValueError()

    @property
    def rounds(self) -> list:
        return self.__rounds

    @rounds.setter
    def rounds(self, value: list):
        if type(value) == list:
            self.__rounds = value
        else:
            raise ValueError()

    @property
    def players(self) -> list:
        return self.__players

    @players.setter
    def players(self, value: list):
        if type(value) == list:
            self.__players = value
        else:
            raise ValueError()

    @property
    def time_rule(self) -> str:
        return self.__time_rule

    @time_rule.setter
    def time_rule(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", value):
            self.__time_rule = value
        else:
            raise ValueError()

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", value):
            self.__description = value
        else:
            raise ValueError()
