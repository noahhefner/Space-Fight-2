# Noah Hefner
# Space Fight 2.0
# Drop Class
# Last Edit: 7/23/2019

import pygame
import settings
from drop_image_strings import drop_image_strings
import random

pygame.init()


class Drop(pygame.sprite.Sprite):
    """
    Powerups that drop when an alien is killed.
    """

    def __init__(self, x_coord, y_coord):

        super(Drop, self).__init__()

        self.drop_type, self.image_string = \
            random.choice(list(drop_image_strings.items()))
        self.image = pygame.image.load(drop_image_strings[self.image_number])
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.dropped_frames = 0

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    def update(self):
        """ Times the drop for dropped_frames. """

        if self.dropped_frames == settings.drop_frames:

            self.kill()
