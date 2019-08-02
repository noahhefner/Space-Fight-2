# Noah Hefner
# Space Fight 2.0
# Alien Class
# Last Edit: 7/23/2019

import math
import pygame
import random

from constants import BLACK
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
        self.pos_initial = self.__random_spawn()
        self.rect.x, self.rect.y = self.pos_initial[0], self.pos_initial[1]
        self.speed = settings["alien_speed"]
        self.drop_carrier = self.__drop_carrier_chance()

        return

    def set_x(self, new_x):

        self.rect.x = new_x

    def set_y(self, new_y):

        self.rect.y = new_y

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    def is_drop_carrier(self):

        return self.drop_carrier

    def __drop_carrier_chance(self):

        cary = random.randrange(0, settings["drop_probability"])

        if not cary:

            return True

        else:

            return False

    def __random_spawn(self):

        position = []
        x = None
        y = None

        left_right = random.randrange(0, 3)

        if left_right == 0:

            x = random.randrange(-600, -100)
            y = random.randrange(-600, settings["screen_height"] + 600)

        elif left_right == 1:

            x = random.randrange(0, settings["screen_width"])

            top_bottom = random.randrange(0, 2)

            if top_bottom == 0:

                y = random.randrange(-600, -100)

            else:

                y = random.randrange(settings["screen_height"] + 100,
                                     settings["screen_height"] + 700)

        else:

            x = random.randrange(settings["screen_width"] + 100,
                                 settings["screen_width"] + 700)
            y = random.randrange(-600, settings["screen_height"] + 600)

        position.append(x)
        position.append(y)

        return position

    def update(self, player_center):
        """
        Auto-calculates path towards player.
        """

        diff_x = player_center[0] - self.rect.center[0]
        diff_y = player_center[1] - self.rect.center[1]

        angle = math.atan2(diff_y, diff_x)

        traj_y = math.sin(angle) * self.speed
        traj_x = math.cos(angle) * self.speed

        self.rect.x += traj_x
        self.rect.y += traj_y

        return True
