"""
Noah Hefner
Space Fight 2.0
Driver Script
Last Edit: 6/28/2020
"""

# Imports
from game_frontend import GameFrontend
from settings import settings
import pygame

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode([settings["screen_width"], settings["screen_height"]])
clock = pygame.time.Clock()

game = GameFrontend(screen, clock)  # Create a game

playing = True

while playing:

    playing = game.update()  # Update game
    game.display()  # Display game
