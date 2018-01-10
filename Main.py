# Noah Hefner
# Space Fight 2.0
# Last Edit: 1/10/2018

# Library Imports
from math import *
from pygame import *
from time import *
from Functions import *
from Explosion import Explosion
from Text import Text
from Button import Button
from Bullet import Bullet
from Alien import Alien
from Drop import Drop
from Game import Game
from Star import Star
from Menu import Menu
from Player import Player
from Settings import Settings
from Scene import Scene
from Array import Array

pygame.init()

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

# Variables
clock = pygame.time.Clock()

# Program Objects
menu = Menu()
settings = Settings()
game = Game(menu.settings)

SCREEN = pygame.display.set_mode([settings.screen_width,\
                                  settings.screen_height])

star_group = pygame.sprite.Group()

for i in range(SCREEN_WIDTH):

    star = Star("star.png")
    star_group.append(star)

while settings.active_screen != "DONE":

    star_group.update()
    star_group.draw(SCREEN)

    while settings.active_screen == "MENU":

        game.settings = menu.game_settings
        menu_done = menu.process_user_events()

    while settings.active_screen == "GAME":

        SCREEN.fill(BLACK)
        game.process_user_events()
        game.display_frame(SCREEN)
        pygame.display.flip()
        clock.tick(60)

pygame.quit
