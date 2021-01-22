""" This module contains the model of a player."""
import re
from typing import Union
from datetime import date
import uuid

from serializable import Serializable


class Player(Serializable):
    """ Class of a model player

    Daughter of the Serializable class. Initiate a list of property to serialize. Property and
    Setter decorators for each property to prevent the user from directly accessing the variables.
    Parameters:
    **params -- dict containing the information of a player

    """
    def __init__(self, **params):
        self.property_list = ['last_name', 'first_name', 'birthdate', 'gender', 'rank']
        super().__init__(self.property_list, **params)

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

    @rank.setter
    def rank(self, value: int):
        if type(value) == int:
            self.__rank = value
        else:
            raise ValueError()
