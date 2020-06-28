"""
Noah Hefner
Space Fight 2.0
Bullet Class
Last Edit: 8/2/2019
"""

# Imports
import math
import pygame
from constants import BLACK
from settings import settings

# Initialize pygame
pygame.init()


class Bullet(pygame.sprite.Sprite):
    """
    In-game bullet entity.

    Attributes:
        image (pygame.image): Image for Bullet sprite.
        rect (pygame.image.rect): Position, height, width values for image.
    """

    def __init__(self, image_string, mouse_pos, player_pos):
        """ Initiate bullet class.
        Args:
            image_string (string): Image path for bullet image.
            x_traj (int): X axis trajectory of the bullet.
            y_traj (int): Y axis trajectory of the bullet.
        """

        super(Bullet, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = player_pos[0]
        self.rect.y = player_pos[1]
        self.mouse_pos = mouse_pos
        self.speed = int(settings["bullet_speed"])
        self.trajectory = self.__calculate_trajectory(mouse_pos, player_pos)

        return

    def update(self):
        """
        Move bullet. Kill bullet when it goes off the screen.
        """

        self.rect.x += self.trajectory[0]
        self.rect.y += self.trajectory[1]

        if self.rect.x + self.rect.width < 0 or \
                self.rect.y + self.rect.height < 0:

            self.kill()

        elif self.rect.y > settings["screen_height"] or \
                self.rect.x > settings["screen_width"]:

            self.kill()

        return True

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

        return True

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

        return True

    def __calculate_trajectory(self, mouse_pos, player_pos):
        """
        Calculate the trajectory of the bullet given player/mouse coordinates.

        Parameters:
            mouse_pos (list): X and Y coordinates of the mouse.
            player_pos (list): X and Y coordinates of the player.
        Returns:
            list: X and Y axis trajectories.
        """

        angle = math.atan2(player_pos[1] - mouse_pos[1],
                           player_pos[0] - mouse_pos[0])
        x_traj = math.cos(angle) * (-1 * self.speed)
        y_traj = math.sin(angle) * (-1 * self.speed)

        return [x_traj, y_traj]
