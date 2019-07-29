# Noah Hefner
# Space Fight 2.0
# Player Class
# Last Edit: 7/21/2019

# Imports
import math
import pygame
from settings import settings

pygame.init()


class Player(pygame.sprite.Sprite):
    """ In-game player entity. """

    def __init__(self, image_string):
        """ Instantiate player class.
        Args:
            image_string (string): name of image file to be used for player.
        """

        super(Player, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey([0, 0, 0])
        self.original = self.image
        self.rect = self.image.get_rect()
        self.set_x(settings["screen_width"] / 2)
        self.set_y(settings["screen_height"] / 2)
        self.bullets = settings["start_bullets"]
        self.lives = settings["start_lives"]
        self.velx = 0
        self.vely = 0

        return

    def set_x(self, new_x):

        self.rect.x = new_x
        settings["player_x_center"] = self.rect.center[0]

    def set_y(self, new_y):

        self.rect.y = new_y
        settings["player_y_center"] = self.rect.center[1]

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    def set_velx(self, velx):

        self.velx += velx
        return True

    def set_vely(self, vely):

        self.vely += vely
        return True

    def change_speed(self, velx, vely):

        self.velx += velx
        self.vely += vely

    def __check_screen_edge_hit(self):
        """ Check if the player is colliding with the edge of the screen. If so,
        stop the player from going off the
        screen. """

        if self.rect.x + self.rect.width >= settings["screen_width"]:
            self.rect.right = settings["screen_width"]

        if self.rect.x <= 0:
            self.rect.left = 0

        if self.rect.y <= 0:
            self.rect.top = 0

        if self.rect.y + self.rect.height >= settings["screen_height"]:
            self.rect.bottom = settings["screen_height"]

    def rotate(self):
        """ Rotate player to face the cursor. """

        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        diff_y = self.rect.center[1] - mouse_y
        diff_x = self.rect.center[0] - mouse_x
        angle = math.degrees(math.atan2(-1 * diff_y, diff_x)) - 180
        self.image = pygame.transform.rotate(self.original, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):

        self.rotate()

        settings["player_x_center"] = self.rect.center[0]
        settings["player_y_center"] = self.rect.center[1]

        self.rect.x += self.velx
        self.rect.y += self.vely

        self.__check_screen_edge_hit()
