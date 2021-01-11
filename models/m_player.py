""" This module contains the model of a player."""
import re
from typing import Union
from datetime import date


class ModelPlayer:
    """ Class of a model player

    Initiate various private variables and store information with a setter to protect the access
    to these variables.
    Parameters:
    last_name -- the last name of the player. Type str.
    first_name -- the first name of the player. Type str.
    birthdate -- the birthdate of the player. Type str or date.
    rank -- ranking of the player. Type int.

    """
    def __init__(self, last_name: str, first_name: str, birthdate: Union[str, date], rank: int):
        incorrect_values = set()

        try:
            self.last_name = last_name
        except ValueError:
            incorrect_values.add("nom")

        try:
            self.first_name = first_name
        except ValueError:
            incorrect_values.add("prénom")

        try:
            self.birthdate = birthdate
        except ValueError:
            incorrect_values.add("date de naissance")

        try:
            self.rank = rank
        except ValueError:
            incorrect_values.add("classement")

        if incorrect_values:
            raise ValueError(f"Paramètres de model player incorrects: {incorrect_values}")

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def last_name_pod(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", value):
            self.__last_name = value
        else:
            raise ValueError()

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def first_name_pod(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z '\-éèàîïùç]{2,}$", value):
            self.__first_name = value
        else:
            raise ValueError()

    @property
    def birthdate(self) -> date:
        return self.__birthdate

    @property
    def birthdate_pod(self) -> str:
        return self.__birthdate.isoformat()

    @birthdate.setter
    def birthdate(self, value: Union[str, date]):
        if type(value) == str and re.match(r"^(\d{4})-(\d{2})-(\d{2})$", value):
            date.fromisoformat(value)
            self.__birthdate = value
        elif type(value) == date:
            self.__birthdate = value
        else:
            raise ValueError()

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def rank_pod(self) -> str:
        return str(self.__rank)

    @rank.setter
    def rank(self, value: int):
        if type(value) == int:
            self.__rank = value
        else:
            raise ValueError()
