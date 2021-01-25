"""This module contains the management of the players"""
from uuid import UUID

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

    def create_player(self, params):
        player = Player(**params)
        self.players[player.identifier_pod] = player.params

    def find_player_by_id(self, id_player: UUID) -> str:
        for player_id in self.players:
            if player_id == id_player:
                return self.players[player_id]


player_manager = PlayerManager()
