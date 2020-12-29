import models.m_player as m_player


class ControlerPlayer:
    def __init__(self):
        self.last_name = ''
        self.first_name = ''
        self.birthdate = ''
        self.rank = 0

        self.m_player = m_player.ModelPlayer(self.last_name, self.first_name, self.birthdate,
                                             self.rank)
        self.player_info = self.m_player.dict_player

    def save_last_name(self, last_name):
        self.player_info['last_name'] = last_name

    def save_first_name(self, first_name):
        self.player_info['first_name'] = first_name

    def save_birthdate(self, birthdate):
        self.player_info['birthdate'] = birthdate

    def save_rank(self, rank):
        self.player_info['rank'] = rank
