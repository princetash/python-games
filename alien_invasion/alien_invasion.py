import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """class to manage assets and behaviour"""

    def __init__(self):
        """initialize the game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height 

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """mainloop of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            self.clock.tick(60)



    def _check_events(self):
            # watch for mouse and key events and respond
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
         #update images on th screen and flip new screens
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        # making the drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
