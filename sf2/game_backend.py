
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

        for i in range(20):

            self.aliens.append(self.__make_alien(self.__find_lvl_1_alien_image()))

    def update(self):

        # Move aliens
        return "boi"

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
