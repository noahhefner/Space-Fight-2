# Noah Hefner
# Space Fight 2.0
# Player Class
# Last Edit: 2.12.2019

import math
import pygame
import time
import Constants

pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, image):

        super(Player, self).__init__()

        self.image = pygame.image.load(image)
        self.image.set_colorkey(Constants.BLACK)
        self.original = self.image
        self.rect = self.image.get_rect()
        self.rect.x = (settings["screen_height"] / 2) - (self.rect.width / 2)
        self.rect.y = (settings["screen_width"] / 2) - (self.rect.height / 2)

        return


    def shift(self, x_shift, y_shift):

        if !(self.rect.x + x_shift < 0) and !(self.rect.x + x_shift > Constants.SCREEN_WIDTH):
            self.rect.x += x_shift

        if !(self.rect.y + y_shift < 0) and !(self.rect.y + y_shift > Constants.SCREEN_HEIGHT):
            self.rect.y += y_shift

        return

    def rotate(self):
        """ Rotate player to face the cursor. """

        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        angle = 360 - (math.degrees(math.atan2(self.rect.center[1] - mouse_y, self.rect.center[0] - mouse_x)) + 180)
        self.image = pygame.transform.rotate(self.original, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        return
