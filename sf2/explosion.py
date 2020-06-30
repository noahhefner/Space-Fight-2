"""
Noah Hefner
Space Fight 2.0
Explosion Class
Last Edit: 6/30/2020
"""

# Imports
import pygame
from constants import BLACK
from strings import image_paths

# Initialize pygame
pygame.init()


class Explosion(pygame.sprite.Sprite):
    """
    Spawns an explosion at the given location.

    Attributes:
        e1 (pygame.image): Image path for frame 1/5 of the explosion.
        e2 (pygame.image): Image path for frame 2/5 of the explosion.
        e3 (pygame.image): Image path for frame 3/5 of the explosion.
        e4 (pygame.image): Image path for frame 4/5 of the explosion.
        e5 (pygame.image): Image path for frame 5/5 of the explosion.
        image_list (list): A subscriptable list for easily parsing the frames.
        frame (int): The total frames elapsed in the explosion.
        exp_num (int): Index of currently showing frame.
        image (pygame.image): The image object that gets blited by front end.
        rect (pygame.image.rect): Position, height, width values for image.
    """

    def __init__(self, x, y):
        """
        Initializes explosion class.

        Parameters:
            x (int): X value for the explosion to spawn.
            y (int): Y value for the explosion to spawn.
        """

        super(Explosion, self).__init__()

        self.e1 = pygame.image.load(image_paths["e1"]).convert()
        self.e2 = pygame.image.load(image_paths["e2"]).convert()
        self.e3 = pygame.image.load(image_paths["e3"]).convert()
        self.e4 = pygame.image.load(image_paths["e4"]).convert()
        self.e5 = pygame.image.load(image_paths["e5"]).convert()

        self.e1.set_colorkey(BLACK)
        self.e2.set_colorkey(BLACK)
        self.e3.set_colorkey(BLACK)
        self.e4.set_colorkey(BLACK)
        self.e5.set_colorkey(BLACK)

        self.image_list = [self.e1, self.e2, self.e3, self.e4, self.e5]
        self.frame = 0
        self.exp_num = 0

        self.image = self.e1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """
        Cycles through the exp_list to display the correct frame and kills the
        sprite at the frame limit.
        """

        if self.frame == 16:

            self.kill()

        elif self.frame % 4 == 0:

            self.exp_num += 1

        self.frame += 1
        self.image = self.image_list[self.exp_num]

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

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y
