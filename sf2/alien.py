# Noah Hefner
# Space Fight 2.0
# Alien Class
# Last Edit: 7/21/2019

import math
import pygame
import time

from Functions import *
from drop import Drop
from constants import *
from settings import settings

pygame.init()

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

        if random.randrange(0, settings.drop_probability) == 1:
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

    def move(self):
        """
        Auto-calculates path towards player.
        """

        diff_x = settings["player_x_center"] - self.rect.center[0]
        diff_y = settings["player_y_center"] - self.rect.center[1]

        angle = math.atan2(diff_y, diff_x)

        traj_y = math.sin(angle) * settings["alien_speed"]
        traj_x = math.cos(angle) * settings["alien_speed"]

        self.rect.x += traj_x
        self.rect.y += traj_y

        return True
