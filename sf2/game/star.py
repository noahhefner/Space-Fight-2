"""
Noah Hefner
Space Fight 2.0
Star Class
Last Edit: 6/28/2020
"""

# Imports
import pygame
import random
from sf2.common.constants import BLACK
from sf2.common.settings import settings_program

# Initialize pygame
pygame.init()


class Star(pygame.sprite.Sprite):
    """
    Star image used to create background.

    Attributes:
        image (pygame.image): Image for Star sprite.
        rect (pygame sprite rect): Rect attributes for sprite image.
        velyt (int): Y-axis velocity of star.
    """

    def __init__(self, image_string):
        """
        Instantiate a Star object.

        Parameters:
            image_string (string): Path of image file for the star.
        """

        super(Star, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, settings_program["screen_width"])
        self.rect.y = random.randrange(0, settings_program["screen_height"])
        self.vely = random.randrange(-3, 0)

    def update(self):
        """
        Move star, reset position if it goes off the top of the screen.
        """

        self.rect.y += self.vely

        if self.rect.y + self.rect.height < 0:

            self.set_y(settings_program["screen_height"])

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

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y
