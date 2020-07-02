"""
Noah Hefner
Space Fight 2.0
Drop Class
Last Edit: 6/28/2020
"""

# Imports
import pygame
import random
from sf2.common.settings import settings_game
from sf2.common.strings import image_paths

# Initialize pygame
pygame.init()


class Drop(pygame.sprite.Sprite):
    """
    Powerups that drop when an alien is killed.

    Attributes:
        image_string (str): Image path for drop image. This is randomly chosen.
        rect (pygame.image.rect): Position, height, width values for image.
        dropped_frames (int): Number of frames that the drop has existed.
    """

    def __init__(self, x_coord, y_coord):

        super(Drop, self).__init__()

        self.image_string = random.choice([image_paths["drop_life"],
                                           image_paths["drop_coin"],
                                           image_paths["drop_bullets"]])
        self.image = pygame.image.load(self.image_string)
        self.rect = self.image.get_rect()
        self.set_x(x_coord)
        self.set_y(y_coord)
        self.dropped_frames = 0

    def update(self):
        """
        Times the drop for dropped_frames. Kills drop at frame limit.
        """

        if self.dropped_frames == int(settings_game["drop_frames"]):

            self.kill()

    def get_type(self):
        """
        Gets the image path of the drop.

        Returns:
            self.image_string (str): Image path of the drop.
        """

        return self.image_string

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
