# Noah Hefner
# Space Fight 2.0
# Player Class
# Last Edit: 7/21/2019

# Imports
import math
import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    """ In-game player entity. """

    def __init__(self, image_string):
        """ Instantiate player class.
        Args:
            image_string (string): name of image file to be used for player image.
        """

        super(Player, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey([0, 0, 0])
        self.original = self.image
        self.rect = self.image.get_rect()
        self.ammo = 100
        self.lives = 3

        return True

    def set_x(self, new_x):

        self.rect.x = new_x

    def set_y(self, new_y):

        self.rect.y = new_y

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    """
    Precondition: x and y are integers
    """
    def move(self, x, y):

        self.rect.x += x
        self.rect.y += y

        self.check_screen_edge_hit()

        settings["player_x_center"] = self.rect.center[0]
        settings["player_y_center"] = self.rect.center[1]

        return True

    def check_screen_edge_hit(self):
        """ Check if the player is colliding with the edge of the screen. If so, stop the player from going off the
        screen. """

        if self.rect.x + self.rect.width >= settings["screen_width"]:
            self.rect.right = settings["screen_width"]

        if self.rect.x <= 0:
            self.rect.left = 0

        if self.rect.y <= 0:
            self.rect.top = 0

        if self.rect.y + self.rect.height >= settings["screen_height"]:
            self.rect.bottom = settings["screen_height"]

    def rotate_player(self):
        """ Rotate player to face the cursor. """

        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(self.rect.center[1] - mouse_y, self.rect.center[0] - mouse_x)) - 180
        self.image = pygame.transform.rotate(self.original, angle)
        self.rect = self.image.get_rect(center = self.rect.center)
