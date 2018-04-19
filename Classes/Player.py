# Noah Hefner
# Space Fight 2.0
# Player Class
# Last Edit: 1/2/2017

import math
import pygame
import time

from Settings import settings

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

pygame.init()

class Player(pygame.sprite.Sprite):
    """ In-game player entity. """

    def __init__(self, image_string):
        """ Initiate player class.
        Args:
            image_string (string): name of image file to be used for player image.
        """

        super(Player, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.original = self.image
        self.rect = self.image.get_rect()
        self.rect.x = (settings["screen_height"] / 2) - (self.rect.width / 2)
        self.rect.y = (settings["screen_width"] / 2) - (self.rect.height / 2)
        self.vel_x = None
        self.vel_y = None
        self.ammo = 100
        self.special = "special image"

    def change_speed(self, x, y):
        """ Adds an int value to the vel_x and vel_y attributes.
        Args:
            x (int): pixel amount to be added to the vel_x attribute.
            y (int): pixel amount to be added to the vel_y attribute.
        """

        self.vel_x += x
        self.vel_y += y

    def check_screen_edge_hit(self):
        """ Check if the player is colliding with the edge of the screen. If so, stop the player from going off the
        screen. """

        if self.rect.x + self.rect.width >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.x <= 0:
            self.rect.left = 0

        if self.rect.y <= 0:
            self.rect.top = 0

        if self.rect.y + self.rect.height >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def rotate_player(self):
        """ Rotate player to face the cursor. """

        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        angle = 360 - (math.degrees(math.atan2(self.rect.center[1] - mouse_y, self.rect.center[0] - mouse_x)) + 180)
        self.image = pygame.transform.rotate(self.original, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_player(self):
        """ Move the position of the player. """

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def update(self):
        """ Checks edge-of-screen collision, move and rotate player. """

        self.check_screen_edge_hit()
        self.rotate_player()
        self.move_player()
