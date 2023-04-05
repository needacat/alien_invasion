class GameStats:
    def __init__(self, settings):
        self.ships_left = None
        self.settings = settings
        self.game_active = False

        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
