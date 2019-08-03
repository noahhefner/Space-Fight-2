"""
Noah Hefner
Space Fight 2.0
Driver Script
Last Edit: 8/3/2019
"""

# Imports
from game_frontend import GameFrontend
import pygame

pygame.init()  # Initialize pygame

game = GameFrontend()  # Create a game

playing = True

while playing:

    playing = game.update()  # Update game
    game.display()  # Display game
