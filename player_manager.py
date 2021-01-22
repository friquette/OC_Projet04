"""This module contains the management of the players"""
from uuid import uuid4


class PlayerManager:
    """ Class of a player manager

    This class contains two methods. id_verification: verifies if the id generated is already attributed.
    player_verification: verifies if the player created is already in the database.

    Parameters:
    players -- dict of all the players
    current_id -- uuid created with the new player
    current_player -- dict of the new player created

    """

    def __init__(self, players: dict, current_id: str, current_player: dict):
        self.players = players
        self.current_id = current_id
        self.current_player = current_player

    def id_verification(self) -> str:
        while True:
            if self.current_id not in self.players:
                return self.current_id
            else:
                self.current_id = str(uuid4())
                continue

    def player_verification(self):
        if self.current_player in self.players.values():
            raise ValueError("Joueur déjà présent dans la base de données")
