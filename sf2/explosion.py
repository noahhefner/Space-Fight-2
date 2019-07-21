# Noah Hefner
# Space Fight 2.0
# Explosion Class
# Last Edit: 12/17/2017

import math
import pygame
import time

pygame.init()

class Explosion(pygame.sprite.Sprite):
    """ Spawns an explosion at the given location. """

    def __init__(self, x, y):
        """ Initializes explosion class.
        Args:
            x (int): x value for the explosion to spawn
            y (int): y value for the explosion to spawn
        """

        super(Explosion, self).__init__()

        self.e1 = pygame.image.load("Space-Fight-2/sf2/resources/images/e1.png").convert()
        self.e2 = pygame.image.load("Space-Fight-2/sf2/resources/images/e2.png").convert()
        self.e3 = pygame.image.load("Space-Fight-2/sf2/resources/images/e3.png").convert()
        self.e4 = pygame.image.load("Space-Fight-2/sf2/resources/images/e4.png").convert()
        self.e5 = pygame.image.load("Space-Fight-2/sf2/resources/images/e5.png").convert()

        self.e1.set_colorkey(BLACK)
        self.e2.set_colorkey(BLACK)
        self.e3.set_colorkey(BLACK)
        self.e4.set_colorkey(BLACK)
        self.e5.set_colorkey(BLACK)

        self.image_list = [self.e1,self.e2,self.e3,self.e4,self.e5]
        self.frame = 0
        self.exp_num = 0

        self.image = self.e1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):

        if self.frame == 16:

            self.kill()

        elif self.frame % 4 == 0:

            self.exp_num += 1

        self.frame += 1
        self.image = self.image_list[self.exp_num]
