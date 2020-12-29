class ModelPlayer:
    def __init__(self, last_name, first_name, birthdate, rank):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.rank = rank

        self.dict_player = {'last_name': self.last_name,
                            'first_name': self.first_name,
                            'birthdate': self.birthdate,
                            'rank': self.rank}

