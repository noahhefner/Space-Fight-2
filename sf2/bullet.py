# Noah Hefner
# Space Fight 2.0
# Bullet Class
# Last Edit: 7/23/2019

import pygame
import math

from settings import settings
from constants import BLACK

pygame.init()


class Bullet(pygame.sprite.Sprite):
    """ In-game bullet entity. """

    def __init__(self, image_string, mouse_pos):
        """ Initiate bullet class.
        Args:
            image_string (string): image path to be used for bullet image.
            x_traj (int): x axis trajectory of the bullet.
            y_traj (int): y axis trajectory of the bullet.
        """

        super(Bullet, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = settings["player_x_center"]
        self.rect.y = settings["player_y_center"]
        self.mouse_pos = mouse_pos
        self.trajectory = self.__calculate_trajectory()

        return

    def __calculate_trajectory(self):

        angle = math.atan2(
            settings["player_x_center"] - self.mouse_pos[0],
            settings["player_y_center"] - self.mouse_pos[1])

        x_traj = math.cos(angle) * settings["bullet_speed"] * -1
        y_traj = math.sin(angle) * settings["bullet_speed"]

        return [x_traj, y_traj]

    def get_x(self):

        return self.rect.x

    def get_y(self):

        return self.rect.y

    def update(self):
        """ Move bullet. This method has an auto-kill. """

        self.rect.x += self.trajectory[0]
        self.rect.y += self.trajectory[1]

        if self.rect.x + self.rect.width < 0 or \
                self.rect.y + self.rect.height < 0:

            self.kill()

        elif self.rect.y > settings["screen_height"] or \
                self.rect.x > settings["screen_width"]:

            self.kill()

        return True
