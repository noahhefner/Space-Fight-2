# Noah Hefner
# Space Fight 2.0
# Last Edit: 11/28/2017

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

pygame.init()

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


#Variables
done = False
game_done = False
menu_done = True
clock = pygame.time.Clock()

game = Game()
menu = Menu()

while not done:

    while not menu_done:

        menu_done =menu.process_user_events()

    while not game_done:

        SCREEN.fill(BLACK)
        game.process_user_events()
        pygame.display.flip()
        clock.tick(60)

    if game_done and menu_done:

        done = True

pygame.quit
