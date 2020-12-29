class ModelTournament:
    def __init__(self, name, location, date, nb_rounds, nb_players, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.nb_rounds = nb_rounds
        self.nb_players = nb_players
        self.players = []
        self.time_control = time_control
        self.description = description

        self.dict_tournament = {'name': self.name,
                                'location': self.location,
                                'date': self.date,
                                'nb_rounds': self.nb_rounds,
                                'nb_players': self.nb_players,
                                'time_control': self.time_control,
                                'description': self.description}
