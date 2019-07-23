# Header here

import pygame

pygame.init()

from game_frontend import GameFrontend

game = GameFrontend()

playing = True

while playing:

    playing = game.update()

    game.display()
