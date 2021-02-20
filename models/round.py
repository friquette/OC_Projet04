""" This module contains the model of a round."""
from datetime import datetime
from typing import Union
import re

from serializable import Serializable


class Round(Serializable):
    """ Class of a model round

        Daughter of the Serializable class. Initiate a list of property to serialize. Property and
        Setter decorators for each property to prevent the user from directly accessing the variables.
        methodname_pod version used to serialize, converting the variable type into str.

        Parameters:
        **params -- dict containing the information of a round.

        """
    def __init__(self, **params):
        self.property_list = ['name', 'start_date', 'end_date', 'match_list']
        super().__init__(self.property_list, **params)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) == str and re.match(r"^[A-Za-z0-9 '\-éèàîïùç]{2,}$", value):
            self.__name = value
        else:
            raise ValueError()

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @property
    def start_date_pod(self) -> str:
        return self.__start_date.isoformat()

    @start_date.setter
    def start_date(self, value: Union[str, datetime]):
        if type(value) == str and re.match(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$", value):
            datetime.fromisoformat(value)
            self.__start_date = value
        elif type(value) == datetime:
            self.__start_date = value
        else:
            raise ValueError()

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @property
    def end_date_pod(self) -> str:
        return self.__end_date.isoformat()

    @end_date.setter
    def end_date(self, value: Union[str, datetime]):
        if type(value) == str and re.match(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$", value):
            datetime.fromisoformat(value)
            self.__end_date = value
        elif type(value) == datetime:
            self.__end_date = value
        else:
            raise ValueError()

    @property
    def match_list(self) -> list:
        return self.__match_list

    @property
    def match_list_pod(self) -> list:

        # self.__match_list = [match.serialize() for match in self.match_list]
        return self.__match_list

    @match_list.setter
    def match_list(self, value: list):
        if type(value) == list:
            self.__match_list = value
        else:
            raise ValueError()
