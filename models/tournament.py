""" This module contains the model of a tournament."""
import re
from typing import Union, List
from datetime import datetime

from serializable import Serializable
from models.player import Player


class Tournament(Serializable):
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
    def __init__(self, **params):
        self.property_list = ['name', 'location', 'tournament_date', 'nb_round', 'rounds', 'players', 'time_rule', 'description']
        super().__init__(self.property_list, **params)

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
    def players(self, value: List[Player]):
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
