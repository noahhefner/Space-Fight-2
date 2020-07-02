"""
Noah Hefner
Space Fight 2.0
Settings Dictionary
Last Edit: 6/28/2020
"""

# Imports
from .strings import image_paths, font_paths
import pygame

# Initialize pygame
pygame.init()


# Holds a bunch of values for the game settings
settings_game = {

    "player_type_string": image_paths["player_white"],
    "bullet_type_string": image_paths["bullet_green"],
    "cursor_type_string": image_paths["cursor_red"],
    "start_bullets": 100,
    "start_lives": 3,
    "player_speed": 6,
    "bullet_speed": 15,
    "coins": 0,
    "alien_speed": 1.5,
    "drop_probability": 10,
    "drop_frames": 600,
    "drop_lives": 1,
    "drop_bullets": 50,
    "drop_coins": 2,
    "hud_spacing": 10,
    "font": pygame.font.Font(font_paths["arcade_classic"], 40),
    "random_value" : 6

}

settings_program = {

    "screen_width": 1000,
    "screen_height": 800,
    "fps": 60

}
