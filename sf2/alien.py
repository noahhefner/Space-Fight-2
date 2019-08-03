"""
Noah Hefner
Space Fight 2.0
Alien Class
Last Edit: 8/2/2019
"""

import math
import pygame
import random

from constants import BLACK
from settings import settings

pygame.init()  # Initialize pygame


class Alien(pygame.sprite.Sprite):
    """
    In-game alien entity.

    Attributes:
        image (pygame.image): Image for alien sprite.
        rect (pygame.image.rect): Position, height, width values for image.
        drop_carrier (bool): True if alien is a drop carrier.
        speed (int): Speed multiplier for aliem movement.
    """

    def __init__(self, image_string):
        """
        Instantiate an alien object.

        Parameters:
            image_string (string): Path of image file to be used for alien.
        """

        super(Alien, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.__random_spawn()

        self.drop_carrier = self.__drop_carrier_chance()
        self.speed = settings["alien_speed"]

        return

    def update(self, player_center):
        """
        Calculates path towards player and moves alien.

        Parameters:
            player_center (tuple): Coordinates of player object.
        """

        diff_x = player_center[0] - self.rect.center[0]
        diff_y = player_center[1] - self.rect.center[1]

        angle = math.atan2(diff_y, diff_x)

        traj_y = math.sin(angle) * self.speed
        traj_x = math.cos(angle) * self.speed

        self.rect.x += traj_x
        self.rect.y += traj_y

        return True

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

        return True

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

        return True

    def is_drop_carrier(self):
        """
        Get boolean of drop_carrier attribute.

        Returns:
            self.drop_carrier (bool): True for carrier, False for non-carrier.
        """

        return self.drop_carrier

    def __drop_carrier_chance(self):
        """
        Generate True or False given drop probability in settings.

        Returns:
            boolean: True if alien is carrier, False if alien is not a carrier.
        """

        carrier = random.randrange(0, settings["drop_probability"])

        if not carrier:

            return True

        else:

            return False

    def __random_spawn(self):
        """
        Generate random spawn point.

        Returns:
            list (int): X and Y coordinates for random spawn location.
        """

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
