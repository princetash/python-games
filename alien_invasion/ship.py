import pygame


class Ship:
    """manages the ship"""

    def __init__(self, ai_game):
        """initialize the game and set its initial position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.get_rect()

        # loading the ship image to the rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the ships exact horizontal position
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship position based on movement flag"""

        #update the ships x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.x += 1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # self.rect.x -= 1
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
