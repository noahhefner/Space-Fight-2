"""
Noah Hefner
Space Fight 2.0
Player Class
Last Edit: 8/2/2019
"""

# Imports
import math
import pygame
from settings import settings

pygame.init()  # Initialize pygame


class Player(pygame.sprite.Sprite):
    """
    In-game player entity.

    Attributes:
        image (pygame.image): Image for player sprite.
        original (pygame.image): Same as image. Used for rotation.
        rect (pygame.image.rect): Position, height, width values for image.
        bullets (int): Number of bullets the player has.
        lives (int): Number of lives the player has.
        velx (int): Velocity of player on x axis.
        vely (int): Velocity of player on y axis.
    """

    def __init__(self, image_string):
        """
        Instantiate a player object.

        Parameters:
            image_string (string): Path of image file to be used for player.
        """

        super(Player, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey([0, 0, 0])
        self.original = self.image
        self.rect = self.image.get_rect()
        self.velx = 0
        self.vely = 0

        self.bullets = settings["start_bullets"]
        self.lives = settings["start_lives"]

        # Set starting position for player
        self.set_x(settings["screen_width"] / 2)
        self.set_y(settings["screen_height"] / 2)

        return

    def update(self):
        """
        Rotate and move player, then check for screen edge collision.
        """

        self.__rotate()
        self.__move()
        self.__check_screen_edge_hit()

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

    def change_speed(self, velx, vely):
        """
        Change speed of player on x and y axis.

        Parameters:
            velx (int): X axis velocity for player.
            vely (int): Y axis velocity for player.
        """

        self.velx += velx
        self.vely += vely

        return True

    def __check_screen_edge_hit(self):
        """
        Prevents the player from moving off the window.
        """

        if self.rect.x + self.rect.width >= settings["screen_width"]:
            self.rect.right = settings["screen_width"]

        if self.rect.x <= 0:
            self.rect.left = 0

        if self.rect.y <= 0:
            self.rect.top = 0

        if self.rect.y + self.rect.height >= settings["screen_height"]:
            self.rect.bottom = settings["screen_height"]

        return True

    def __move(self):
        """
        Move the player according to x and y axis velocities.
        """

        self.rect.x += self.velx
        self.rect.y += self.vely

        return True

    def __rotate(self):
        """
        Rotates the player to face the cursor.
        """

        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        diff_y = self.rect.center[1] - mouse_y
        diff_x = self.rect.center[0] - mouse_x
        angle = math.degrees(math.atan2(-1 * diff_y, diff_x)) - 180
        self.image = pygame.transform.rotate(self.original, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        return True
