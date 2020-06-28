"""
Noah Hefner
Space Fight 2.0
Cursor Class
Last Edit: 6/28/2020
"""

# Imports
import pygame
from constants import BLACK

# Initialize pygame
pygame.init()


class Cursor(pygame.sprite.Sprite):
    """
    Cursor that is blitted in place of the system cursor.

    Attributes:
      image (pygame.image): Image for cursor sprite.
      rect (pygame sprite rect): Rect attributes for sprite image.
    """

    def __init__(self, cursor_image):
        """
        Initialize a Cursor object.

        Parameters:
            image_string (str): Path of image file used for cursor.
        """

        super(Cursor, self).__init__()

        self.image = pygame.image.load(cursor_image)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self, mouse_pos):
        """
        Set center of cursor to the mouse position.
        """

        self.rect.center = (mouse_pos[0], mouse_pos[1])

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
