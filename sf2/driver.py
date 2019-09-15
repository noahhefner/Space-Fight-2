"""
Noah Hefner
Space Fight 2.0
Driver Script
Last Edit: 9/15/2019
"""

# Imports
from game import Game
import pygame

pygame.init()  # Initialize pygame

size = [800, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Menu Demo")
clock = pygame.time.Clock()

game = Game(screen)  # Create a game

playing = True

while playing:

    user_events = pygame.event.get()

    playing = game.update(user_events)  # Update game

    game.display()  # Display game
