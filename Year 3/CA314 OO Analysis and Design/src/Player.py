class Player:
    def __init__(self, name, player_colour, language, turn):
        self.name = name
        self.record = None
        self.colour = player_colour
        self.language = language
        self.turn = turn

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_record(self, new_record):
        self.record = new_record

    def get_record(self):
        return self.record

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

    def set_turn(self, turn):
        self.turn = turn

    def get_turn(self):
        return self.turn

    def get_all(self):
        return self.name, self.record, self.colour, self.language, self.turn
