import utility as utils
import controllers.c_player as c_player


class PlayerView:
    def __init__(self):
        # self.utils = utils.Utils()
        self.c_player = c_player.PlayerController()
        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.rank = None

    def display_player_questions(self):
        self.c_player.start()
        print("test: ", self.c_player)
