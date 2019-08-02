# Noah Hefner
# Space Fight 2.0
# Driver Script
# Last Edit: 8/2/2019

from game_frontend import GameFrontend
import pygame

pygame.init()

game = GameFrontend()

playing = True

while playing:

    playing = game.update()
    game.display()
