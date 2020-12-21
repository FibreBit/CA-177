class Rules:
    def __init__(self):
        #Default rules for the game.
        self.board_size = 15
        self.turn_time_limit = 45 #seconds
        self.game_time_limit = 30 #minutes
        self.rack_size = 7

    def set_board_size(self, new_board_size):
        self.board_size = new_board_size

    def set_turn_time_limit(self, time):
        self.turn_time_limit = time

    def set_game_time_limit(self, game_time):
        self.game_time_limit = game_time

    def set_rack_size(self, new_rack_size):
        self.rack_size = new_rack_size

    def get_details(self):
        print("{} {} {} {}".format(self.board_size, self.turn_time_limit, self.game_time_limit, self.rack_size))
        return
