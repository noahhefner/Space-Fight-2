# Noah Hefner
# Space Fight 2.0
# Main (run this to start program)
# Last Edit: 4/28/2018

# Library Imports
import math
import pygame
import time

pygame.init()

# Import all the classes
from Explosion import Explosion
from Button import Button
from Bullet import Bullet
from Alien import Alien
from Functions import *
from Drop import Drop
from Game import Game
from Star import Star
from Menu import Menu
from Cursor import Cursor
from Player import Player
from Settings import settings
from Array import Array
from random import *
import Constants

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

screen = pygame.display.set_mode([settings["screen_width"], settings["screen_height"]], pygame.FULLSCREEN)

# Variables
clock = pygame.time.Clock()

# Program Objects
menu = Menu()
game = Game()
cursor = Cursor(settings["cursor_type_string"])

menu_done = False
reset = False

# Stars are not part of menu or game
star_group = pygame.sprite.Group()

# Create background stars
for i in range(settings["screen_width"]):

    star = Star("/home/noahhefner/Git/Space-Fight-2/Images/star.png", settings["screen_width"], settings["screen_height"])
    star_group.add(star)

# While the program is running
while settings["active_screen"] != "done":

    # Updates
    star_group.update()
    cursor.update()

    # Draw background first
    screen.fill(Constants.BLACK)

    # Draw active elements
    star_group.draw(screen)

    # Draw menu items if menu is active screen
    if settings["active_screen"] == "menu":

        menu.update()
        menu.process_user_events()
        menu.display_frame(screen)
        draw_sprite(cursor, screen)


    # Draw settings items if settings is active screen
    if settings["active_screen"] == "game":

        game.process_user_events()
        reset = game.run_game_logic()
        game.display_frame(screen)


    if reset:

        game.__init__()

    pygame.display.flip()
    clock.tick(60)

pygame.quit
