"""This module contains the management of the players"""
from tinydb import TinyDB

from models.tournament import Tournament


class TournamentManager:
    """ Class of a player manager

    This class contains two methods. id_verification: verifies if the id generated is already attributed.
    player_verification: verifies if the player created is already in the database.

    Parameters:
    players -- dict of all the players
    current_id -- uuid created with the new player
    current_player -- dict of the new player created

    """

    def __init__(self):
        self.tournaments = {}
        self.tournament = None

    def create_tournament(self, params):
        self.tournament = Tournament(**params)
        self.tournaments[self.tournament.identifier] = self.tournament.params

    def find_tournament_by_id(self, id_tournament: str) -> str:
        for tournament_id in self.tournaments:
            if tournament_id == id_tournament:
                return self.tournaments[tournament_id]

    def save_tournament_in_db(self):
        db = TinyDB('database.json')
        table = db.table('tournaments')
        self.tournament.serialize()
        table.insert(self.tournament.params)

    def load_tournament_from_db(self):
        db = TinyDB('database.json')
        table = db.table('tournaments')
        for item in table:
            self.create_tournament(item)


tournament_manager = TournamentManager()
