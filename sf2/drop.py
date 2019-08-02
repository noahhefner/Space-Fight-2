# Noah Hefner
# Space Fight 2.0
# Drop Class
# Last Edit: 8/2/2019

import pygame
from settings import settings
from strings import image_paths
import random

pygame.init()


class Drop(pygame.sprite.Sprite):
    """
    Powerups that drop when an alien is killed.
    """

    def __init__(self, x_coord, y_coord):

        super(Drop, self).__init__()

        self.image_string = random.choice([image_paths["drop_life"],
                                           image_paths["drop_coin"],
                                           image_paths["drop_bullets"]])
        self.image = pygame.image.load(self.image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.dropped_frames = 0

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    def get_type(self):

        return self.image_string

    def update(self):
        """ Times the drop for dropped_frames. """

        if self.dropped_frames == int(settings["drop_frames"]):

            self.kill()
