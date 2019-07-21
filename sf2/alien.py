# Noah Hefner
# Space Fight 2.0
# Alien Class
# Last Edit: 4/24/2018s

import math
import pygame
import time

from Functions import *
from drop import Drop
from Settings import settings

pygame.init()

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

class Alien(pygame.sprite.Sprite):
    """ In game alien entity. """

    def __init__(self, image_string):
        """ Initiate alien class. """

        super(Alien, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos_initial = random_alien_spawn(settings["screen_width"], settings["screen_height"])
        self.rect.x, self.rect.y = self.pos_initial[0], self.pos_initial[1]
        self.speed = settings["alien_speed"]
        self.drop = None

        if random.randrange(0,settings.drop_probability) == 1:
            self.drop = Drop()

        return

    def set_x(self, new_x):

        self.rect.x = new_x

    def set_y(self, new_y):

        self.rect.y = new_y

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    """
    Precondition: x and y are integers
    """
    def move(self, x, y):

        self.rect.x += x
        self.rect.y += y

        return True
