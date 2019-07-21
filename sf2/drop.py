# Noah Hefner
# Space Fight 2.0
# Drop Class
# Last Edit: 7/21/2019

import math
import pygame
import time

pygame.init()

class Drop(pygame.sprite.Sprite):
    """ Powerups that drop when an alien is killed. """
    """ Restrict usage of this method to only recieve sprites with drops. """

    def __init__(self, alien):

        super(Drop, self).__init__()

        drop_image_list = ["/Space-Fight-2/Images/drop_ammo.png", \
        "/Space-Fight-2/Images/drop_coin.png", \
         "/Space-Fight-2/Images/drop_life.png"]

        self.image_number = random.randrange(0, 3)
        self.image = pygame.image.load(drop_image_list[self.image_number])
        self.rect = self.image.get_rect()
        self.rect.x = (alien.rect.x + (alien.rect.width / 2)) - self.rect.width /  2
        self.rect.y = (alien.rect.y + (alien.rect.height / 2)) - self.rect.height / 2
        self.dropped_frames = 0

    def update(self):
        """ Times the drop for dropped_frames. """

        if self.dropped_frames == 400:

            self.kill()
