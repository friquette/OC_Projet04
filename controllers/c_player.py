import utility as utls
import models.m_player as m_player


class PlayerController:
    def __init__(self):
        self.utils = utls.Utils()

        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.rank = None

        self.m_player = None

    def get_player_info(self):
        self.last_name = self.utils.ask_pattern("Nom: ")
        self.first_name = self.utils.ask_pattern("Prenom: ")
        self.birthdate = self.utils.ask_date("Date de naissance: ")
        self.rank = self.utils.ask_int("Classement: ")

        self.m_player = m_player.ModelPlayer(self.last_name, self.first_name, self.birthdate,
                                             self.rank)