"""This module contains the management of the players"""
from uuid import UUID

from tinydb import TinyDB

from models.player import Player


class PlayerManager:
    """ Class of a player manager

    This class contains two methods. id_verification: verifies if the id generated is already attributed.
    player_verification: verifies if the player created is already in the database.

    Parameters:
    players -- dict of all the players
    current_id -- uuid created with the new player
    current_player -- dict of the new player created

    """

    def __init__(self):
        self.players = {}
        self.player = None

    def create_player(self, params):
        self.player = Player(**params)
        self.players[self.player.identifier_pod] = self.player.params

    def find_player_by_id(self, id_player: str) -> str:
        for key, value in self.players.items():
            if key == id_player:
                return self.players[key]

    def save_player_in_db(self):
        db = TinyDB('database.json')
        table = db.table('players')
        self.player.serialize()
        table.insert(self.player.params)

    def load_player_from_db(self):
        db = TinyDB('database.json')
        table = db.table('players')
        for item in table:
            self.create_player(item)


player_manager = PlayerManager()
