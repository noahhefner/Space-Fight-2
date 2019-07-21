# Noah Hefner
# Space Fight 2.0
# GameBackend Class
# Last Edit: 7/21/2019

# Imports
from .player import Player
from .bullet import Bullet
from .alien import Alien
from .settings import settings
import pygame

pygame.init()

class GameBackend:

    def __init__(self):
        self.settings = settings
        self.player = Player(self.__find_player_image())

        self.bullets = []
        self.aliens = []
        self.explosions = []
        self.drops = []

        for i in range(20):

            self.aliens.append(self.__make_alien(self.__find_lvl_1_alien_image()))

    def update(self):

        """
        Things that should happen here:
            - Get user input

            - Move Player
            - Move aliens
                - Calculate trajectory towards player
            - Move bullets

            - Hit detection

            - Update player lives
            - Update player bullets
            - Update explosions
            - Update remaining time for any drops

        Returns:
            - True if the game should continue
            - False if the game should be ended
        """

    def __find_player_image(self):
        return "player image"

    def __find_bullet_image(self):

        return "bullet image"

    def __find_lvl_1_alien_image(self):

        return "alien level 1 image"

    def __find_lvl_2_alien_image(self):
        return "alien level 2 image"

    def __find_lvl_3_alien_image(self):
        return "alien level 3 image"

    def __make_bullet(self):

        bullet = Bullet(self.__find_bullet_image())
        self.bullets.append(bullet)

    def __make_alien(self, image_string):

        return Alien(image_string)
