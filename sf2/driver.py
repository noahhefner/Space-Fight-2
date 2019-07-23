# Header here

from game_frontend import GameFrontend
import pygame

pygame.init()


game = GameFrontend()

playing = True

while playing:

    playing = game.update()

    game.display()
