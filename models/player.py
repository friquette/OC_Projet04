""" This module contains the model of a player."""
import re
from typing import Union
from datetime import date
from uuid import UUID
from enum import Enum

from serializable import Serializable


class Gender(Enum):
    HOMME = 1
    FEMME = 2

    def __str__(self):
        return self.name


class Player(Serializable):
    """ Class of a model player

    Daughter of the Serializable class. Initiate a list of property to serialize. Property and
    Setter decorators for each property to prevent the user from directly accessing the variables.
    Parameters:
    **params -- dict containing the information of a player

    """
    def __init__(self, **params):
        self.property_list = ['identifier', 'last_name', 'first_name', 'birthdate', 'gender', 'rank']
        super().__init__(self.property_list, **params)


    @property
    def identifier(self) -> UUID:
        return self.__identifier

    @property
    def identifier_pod(self) -> str:
        return str(self.identifier)

    @identifier.setter
    def identifier(self, value: Union[UUID, str] = None):
        if type(value) == str and re.match(r"^[a-z0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}$", value):
            self.__identifier = UUID(value)
        elif type(value) == UUID:
            self.__identifier = value
        else:
            raise ValueError()


    @property
    def last_name(self) -> str:
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
        return self.birthdate.isoformat()

    @birthdate.setter
    def birthdate(self, value: Union[str, date]):
        if type(value) == str and re.match(r"^(\d{4})-(\d{2})-(\d{2})$", value):
            self.__birthdate = date.fromisoformat(value)
        elif type(value) == date:
            self.__birthdate = value
        else:
            raise ValueError()

    @property
    def gender(self) -> Gender:
        return self.__gender

    @property
    def gender_pod(self) -> str:
        return self.__gender.name

    @gender.setter
    def gender(self, value: Union[Gender, str]):
        if type(value) == str and re.match(r"HOMME", value):
            self.__gender = Gender[value]
        elif type(value) == str and re.match(r"FEMME", value):
            self.__gender = Gender[value]
        elif type(value) == Gender:
            self.__gender = value
        else:
            raise ValueError()

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, value: Union[str, int]):
        if type(value) == str:
            self.__rank = int(value)
        elif type(value) == int:
            self.__rank = value
        else:
            raise ValueError()
