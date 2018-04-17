# Noah Hefner
# Space Fight 2.0
# Main (run this to start program)
# Last Edit: 3/20/2018

# TODO: Make functions for writing and reading settings dict

# Library Imports
import math
import pygame
import time

pygame.init()

from Explosion import Explosion
from Button import Button
from Bullet import Bullet
from Alien import Alien
from Drop import Drop
from Game import Game
from Star import Star
from Menu import Menu
from Player import Player
from Settings import settings
from Array import Array
from random import *

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

screen = pygame.display.set_mode([settings["screen_width"], settings["screen_height"]])

# Variables
clock = pygame.time.Clock()

# Program Objects
menu = Menu()
game = Game()

# Stars are not part of menu or game
star_group = pygame.sprite.Group()

for i in range(settings[screen_width]):

    star = Star("star.png")
    star_group.append(star)

while settings[active_screen] != "DONE":

    # Updates
    star_group.update()


    # Draw background first
    screen.fill(BLACK)

    # Draw active elements
    star_group.draw(screen)

    while settings[active_screen] == "MENU":

        game.settings = menu.game_settings
        menu_done = menu.process_user_events()

    while settings[active_screen] == "GAME":

        SCREEN.fill(BLACK)
        game.process_user_events()
        game.display_frame(SCREEN)
        pygame.display.flip()
        clock.tick(60)

pygame.quit
