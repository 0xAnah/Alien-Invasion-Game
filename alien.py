import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the image and set its rect attributes
        self.image = pygame.image.load("Studying Python/alien_invasion/Images/alien.bmp")
        self.rect = self.image.get_rect()

        # start each new alien near the top of the left screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position
        self.x = float(self.rect.x)