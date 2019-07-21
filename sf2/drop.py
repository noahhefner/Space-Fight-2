# Noah Hefner
# Space Fight 2.0
# Drop Class
# Last Edit: 7/21/2019

import math
import pygame
import time
import settings

pygame.init()

class Drop(pygame.sprite.Sprite):
    """
    Powerups that drop when an alien is killed.
    """

    def __init__(self, x_coord, y_coord):

        super(Drop, self).__init__()

        drop_image_list = [
        "/Space-Fight-2/sf2/resources/images/drop_ammo.png",
        "/Space-Fight-2/sf2/resources/images/drop_coin.png",
        "/Space-Fight-2/sf2/resources/images/drop_life.png"
        ]

        self.image_number = random.randrange(0, 3)
        self.image = pygame.image.load(drop_image_list[self.image_number])
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.dropped_frames = 0

    def update(self):
        """ Times the drop for dropped_frames. """

        if self.dropped_frames == settings.drop_frames:

            self.kill()
