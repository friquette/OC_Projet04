"""This module contains the management of the tournaments"""
from tinydb import TinyDB

from models.tournament import Tournament


class TournamentManager:
    """ Class of a tournament manager

    This class contains methods to create, search or save tournaments. It contains 4 methods:
    create_tournament: create a tournament from the params and puts it in the tournaments dict with
                    the tournament id as the key.
    find_tournament_by_id: verifies if the id is in the tournaments dict and returns the matching tournament.
    save_tournament_in_db: serialize the tournament and saves it in the database under the 'tournaments' table.
    load_tournament_from_db: creates a tournament for each item in the 'tournaments' table.

    """

    def __init__(self):
        self.tournaments = {}
        self.tournament = None

    def create_tournament(self, params):
        self.tournament = Tournament(**params)
        self.tournaments[self.tournament.identifier] = self.tournament.params

    def find_tournament_by_id(self, id_tournament: str) -> str:
        for key, value in self.tournaments.items():
            if key == id_tournament:
                return self.tournaments[key]

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
