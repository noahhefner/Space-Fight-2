"""
Noah Hefner
Space Fight 2.0
Button Class
Last Edit: 6/29/2020
"""

# Imports
import pygame
from .menu_manager_settings import menu_manager_settings

# Initialize pygame
pygame.init()


class Picture(pygame.sprite.Sprite):
    """
    Picture object for menu manager.

    Attributes:
        image (pygame.image): Image for picture.
        rect (pygame.image.rect): Position, height, width values for picture.
    """

    def __init__ (self, image, pos = [0,0]):
        """
        Instantiate a picture object.

        Arguments:
            image (string): Path of image file to be used for picture.
            pos (tuple): XY position for the picture.
        """

        super(Picture, self).__init__()

        self.image = pygame.image.load(image)
        self.image.set_colorkey(menu_manager_settings["element_colorkey"])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_pos (self, pos):
        """
        Set position of the picture.

        Arguments:
            pos (tuple): XY position to set the picture to.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]
