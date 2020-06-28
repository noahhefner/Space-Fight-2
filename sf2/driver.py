"""
Noah Hefner
Space Fight 2.0
Driver Script
Last Edit: 6/28/2020
"""

# Imports
from game_frontend import GameFrontend
import pygame

# Initialize pygame
pygame.init()

game = GameFrontend()  # Create a game

playing = True

while playing:

    playing = game.update()  # Update game
    game.display()  # Display game
