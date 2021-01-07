import utility as utls
import views.v_player as v_player
import models.m_player as m_player


class PlayerController:
    def __init__(self):
        self.player_controller = None
        self.test_dict = {}

    def start(self):
        self.player_controller = LastNamePlayerController()
        self.player_controller()

    def player_dict(self, last_name, first_name, birthdate, rank):
        self.test_dict = {'last_name': last_name,
                          'first_name': first_name,
                          'birthdate': birthdate,
                          'rank': rank}

    def __str__(self):
        # print(self.test_dict)
        for i in self.test_dict.values():
            return i


class LastNamePlayerController:
    def __init__(self):
        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.rank = None
        self.utils = utls.Utils()
        self.m_player = None
        self.v_player = v_player.PlayerView()
        self.player_dict = {}
        self.p_controller = PlayerController()

    def __call__(self):
        self.last_name = self.utils.ask_pattern("Nom: ")
        self.first_name = self.utils.ask_pattern("Prenom: ")
        self.birthdate = self.utils.ask_date("Date de naissance: ")
        self.rank = self.utils.ask_int("Classement: ")

        self.m_player = m_player.ModelPlayer(self.last_name, self.first_name, self.birthdate,
                                             self.rank)

        self.p_controller.player_dict(self.m_player.last_name, self.m_player.first_name, self.m_player.birthdate,
                                      self.m_player.rank)
