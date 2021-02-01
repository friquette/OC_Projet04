from datetime import datetime
from typing import List, Union
import re

from serializable import Serializable
from models.match import Match


class Round(Serializable):
    def __init__(self, **params):
        self.property_list = ['name', 'start_date', 'end_date', 'match_list']
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
    def match_list(self) -> List[Match]:
        return self.__match_list

    @match_list.setter
    def match_list(self, value: List[Match]):
        if type(value) == List[Match]:
            self.__match_list = value
        else:
            raise ValueError()
