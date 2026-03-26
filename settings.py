
class Settings:
    """A class to store all settings for Alien Invasion game"""

    def __init__(self):
        """initialise the game settings"""
        # Screen settings 
        self.screen_height = 500
        self.screen_width = 500
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3