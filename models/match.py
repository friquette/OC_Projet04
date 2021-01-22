"""This module contains the model of a match"""
from models.player import Player
from serializable import Serializable


class Match(Serializable):
    """ Class of a model match

        Daughter of the Serializable class. Initiate a list of property to serialize. Property and
        Setter decorators for each property to prevent the user from directly accessing the variables.
        Parameters:
        **params -- dict containing the information of a match.

        """
    def __init__(self, **params):
        self.property_list = ['player_01', 'player_02', 'player_01_score', 'player_02_score']
        super().__init__(self.property_list, **params)

        # TODO: stocker un match sous la forme : match = (['player_01', 'player_01_score'], ['player_02', 'player_02_score'])

    @property
    def player_01(self) -> Player:
        return self.__player_01

    @player_01.setter
    def player_01(self, value: Player):
        if type(value) == Player:
            self.__player_01 = value
        else:
            raise ValueError()

    @property
    def player_02(self) -> Player:
        return self.__player_02

    @player_02.setter
    def player_02(self, value: Player):
        if type(value) == Player:
            self.__player_02 = value
        else:
            raise ValueError()

    @property
    def player_01_score(self) -> int:
        return self.__player_01_score

    @player_01_score.setter
    def player_01_score(self, value: int):
        if type(value) == int:
            self.__player_01_score = value
        else:
            raise ValueError()

    @property
    def player_02_score(self) -> int:
        return self.__player_02_score

    @player_02_score.setter
    def player_02_score(self, value: int):
        if type(value) == int:
            self.__player_02_score = value
        else:
            raise ValueError()
