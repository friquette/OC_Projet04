import models.m_tournament as m_tournament
import controlers.c_player as c_player


class ControlTournament:
    def __init__(self):
        self.name = ''
        self.location = ''
        self.date = ''
        self.nb_rounds = 4
        self.nb_players = 8
        self.players = []
        self.time_control = ''
        self.description = ''

        self.m_tournament = m_tournament.ModelTournament(self.name, self.location, self.date,
                                                         self.nb_rounds, self.nb_players,
                                                         self.time_control, self.description)

        self.tournament_info = self.m_tournament.dict_tournament
        self.c_player = c_player.ControlPlayer()

    def save_tournament_name(self, name):
        self.tournament_info['name'] = name

    def save_tournament_location(self, location):
        self.tournament_info['location'] = location

    def save_tournament_date(self, date):
        self.tournament_info['date'] = date

    def save_tournament_nb_rounds(self, nb_rounds):
        self.tournament_info['nb_rounds'] = nb_rounds

    def save_tournament_nb_players(self, nb_players):
        self.tournament_info['nb_players'] = nb_players

    def save_tournament_players(self):
        self.tournament_info['players'].append(self.c_player.player_info)

    def save_tournament_time_control(self, time_control):
        self.tournament_info['time_control'] = time_control

    def save_tournament_description(self, description):
        self.tournament_info['description'] = description


