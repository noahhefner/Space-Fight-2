
from .player import Player
import pygame

pygame.init()

class GameBackend():

    def __init__ (self):

        self.player = Player(self.__find_player_image())

    def __find_player_image(self):

        return "string"