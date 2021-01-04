import re
from typing import Union
from datetime import date


class ModelPlayer:
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
    def birthdate(self) -> str:
        return self.__birthdate

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
