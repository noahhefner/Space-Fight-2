# Noah Hefner
# Space Fight 2.0
# Star Class
# Last Edit: 7/21/2019

import pygame
import random
from settings import settings
from constants import BLACK

pygame.init()


class Star(pygame.sprite.Sprite):
    """ Star sprite images used for background. """

    def __init__(self, image_string):

        super(Star, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, settings["screen_width"])
        self.rect.y = random.randrange(0, settings["screen_height"])
        self.vely = random.randrange(-3, 0)

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    def update(self):
        """ Add the velx and vely attributes to the rect.x and rect.y
        positions, respectively. If the star goes off the top of the screen,
        reset the posiiton to the bottom of the screen.

        """

        self.rect.y += self.vely

        if self.rect.y + self.rect.height < 0:

            self.rect.y = settings["screen_height"]
