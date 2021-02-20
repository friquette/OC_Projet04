"""This module contains the management of the players"""
from tinydb import TinyDB

from models.player import Player


class PlayerManager:
    """ Class of a player manager

    This class contains methods to create, search or save players. It contains 4 methods:
    create_player: create a player from the params and puts it in the players dict with the player
                identifier as the key.
    find_player_by_id: verifies if the id is in the players dict and returns the matching player.
    save_player_in_db: serialize the player and saves it in the database under the 'player' table.
    load_player_from_db: create a player for each item in the 'player' table.

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
