import controllers.c_player as c_player


class PlayerView:
    def __init__(self):
        self.c_player = c_player.PlayerController()

    def display_player_questions(self):
        self.c_player.get_player_info()
        print("Joueur: {} {}, né le {}. Classement: {}".format(self.c_player.first_name,
                                                               self.c_player.last_name,
                                                               self.c_player.birthdate,
                                                               self.c_player.rank))
