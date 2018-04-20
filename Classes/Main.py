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

menu_done = False

# Stars are not part of menu or game
star_group = pygame.sprite.Group()

for i in range(settings["screen_width"]):

    star = Star("/home/noahhefner/Git/Space-Fight-2/Images/star.png", settings["screen_width"], settings["screen_height"])
    star_group.add(star)

while settings["active_screen"] != "done":

    # Updates
    star_group.update()

    # Draw background first
    screen.fill(BLACK)

    # Draw active elements
    star_group.draw(screen)

    if settings["active_screen"] == "menu":

        menu.update()
        menu.process_user_events()
        menu.display_frame(screen)

    if settings["active_screen"] == "game":

        game.run_game_logic()
        game.process_user_events()
        game.display_frame(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit
