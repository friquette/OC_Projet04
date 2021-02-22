""" This module contains the model of a tournament."""
import re
from typing import Union, List
from datetime import datetime
from enum import Enum

from serializable import Serializable


class TimeRule(Enum):
    """ The TimeRule class contains three constants: BULLET, BLITZ and RAPID."""

    BULLET = 1
    BLITZ = 2
    RAPID = 3

    def __str__(self):
        return self.name


class Tournament(Serializable):
    """ Class of a model tournament

    Daughter of the Serializable class. Initiate a list of property to serialize. Property and
    Setter decorators for each property to verify the user input is matching what the program expects.
    methodname_pod version used to serialize, converting the variable type into str.

    Parameters:
    **params -- dict containing the information of a tournament.

    """
    def __init__(self, **params):
        self.property_list = ['identifier', 'name', 'location', 'tournament_date', 'nb_round', 'rounds', 'players',
                              'time_rule', 'description']
        super().__init__(self.property_list, **params)

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z0-9 '\-éèàîïùç]{2,}$", value):
            self.__identifier = value
        else:
            raise ValueError()

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
    def tournament_date(self) -> datetime:
        return self.__tournament_date

    @property
    def tournament_date_pod(self) -> str:
        return self.__tournament_date.isoformat()

    @tournament_date.setter
    def tournament_date(self, value: Union[str, datetime]):
        if type(value) == str and re.match(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$", value):
            datetime.fromisoformat(value)
            self.__tournament_date = value
        elif type(value) == str and re.match(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})$", value):
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

    @property
    def rounds_pod(self) -> list:
        self.__rounds = [round.serialize() for round in self.rounds]
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

    @property
    def players_pod(self) -> list:
        self.__players = [player.serialize() for player in self.players]
        return self.__players

    @players.setter
    def players(self, value: List):
        if type(value) == list:
            self.__players = value
        else:
            raise ValueError()

    @property
    def time_rule(self) -> TimeRule:
        return self.__time_rule

    @property
    def time_rule_pod(self) -> str:
        return self.__time_rule.name

    @time_rule.setter
    def time_rule(self, value: Union[TimeRule, str]):
        if type(value) == str and re.match(r"BULLET", value):
            self.__time_rule = TimeRule[value]
        elif type(value) == str and re.match(r"BLITZ", value):
            self.__time_rule = TimeRule[value]
        elif type(value) == str and re.match(r"RAPID", value):
            self.__time_rule = TimeRule[value]
        elif type(value) == TimeRule:
            self.__time_rule = value
        else:
            raise ValueError()

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z0-9 '\-éèàîïùç]{2,}$", value):
            self.__description = value
        else:
            raise ValueError()
