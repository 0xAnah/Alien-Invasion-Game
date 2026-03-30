
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.ship_left = self.settings.ship_limit
        

    def reset_stats(self):
        """Initialize statistics that can chage during the game"""
        self.ship_left = self.settings.ship_limit
        