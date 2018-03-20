# Noah Hefner
# Space Fight 2.0
# Bullet Class
# Last Edit: 12/17/2017

import math
import pygame
import time

pygame.init()

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

class Bullet(pygame.sprite.Sprite):
    """ In-game bullet entity. """

    def __init__(self, image_string):
        """ Initiate bullet class.
        Args:
            image_string (string): name of image file to be used for bullet image.
        """

        super(Bullet, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.vel = Functions.get_bullet_vel(20)

    def update(self):
        """ Move bullet and check for kill. """

        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        if self.rect.x + self.rect.width < 0 or self.rect.y + self.rect.height < 0:

            self.kill()

        elif self.rect.y > SCREEN_HEIGHT or self.rect.x > SCREEN_WIDTH:

            self.kill()
