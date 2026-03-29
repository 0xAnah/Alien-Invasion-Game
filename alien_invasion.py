import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock() # the clock to control the game fps
        self.settings = Settings() # this controls the games settings
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # the game window size
        
        self.ship = Ship(self) # the ship
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")

    def _create_alien(self, x_position, y_position):
        """create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _create_fleet(self):
        """create a fleet of aliens"""
        # create  an alien and keep adding until there's no room left.
        # Spacing between aliens is one alien width 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3* alien_height):
            while current_x < (self.settings.screen_width -2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached and edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """drop the entire fleet and change the fleets direction"""
        for alien in self.aliens.sprites():
            alien.rect.y +=self.settings.fleet_drop_speed
        
        self.settings.fleet_direction *= -1


    def _fire_bullet(self):
        """creats a new bullet and adds it to the group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_event(self, event):
        # check if its the right arrow key
        if event.key == pygame.K_RIGHT:
            # if its the right arrow key move the ship to the right
            self.ship.moving_right = True
        # check if its the left arrow key
        elif event.key == pygame.K_LEFT:
            # if its the left arrow key move the ship to the left
            self.ship.moving_left = True
        # exit the game if the "Q" key is pressed
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        # check if its the right arrow key was released
        if event.key == pygame.K_RIGHT:
            # if it is stop moving the ship to the right
            self.ship.moving_right = False
        # check if its the left arrow key
        elif event.key == pygame.K_LEFT:
            # if it is stop moving the ship to the left
            self.ship.moving_left = False

    def _check_event(self):
        """This manages the events of the game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # check if a key has been pressed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            # check if a key has been released
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)


    def _update_bullets(self):
            """Update position of bullets and get rid of old bullets."""
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # set the background color during each pass of the loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        # Make the most recently drawn screen visible
        pygame.display.flip()
        

    def _update_aliens(self):
        """check if the fleet is at the edge then update the positions"""
        self._check_fleet_edges()
        self.aliens.update()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self._update_aliens()
            self.clock.tick(60)


if __name__ == "__main__":
    # make a game instance and run the game
    ai_game = AlienInvasion()
    ai_game.run_game()