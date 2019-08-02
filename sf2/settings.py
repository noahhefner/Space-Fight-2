# Noah Hefner
# Space Fight 2.0
# Settings Dictionary
# Last Edit: 8/2/2019

from strings import image_paths, font_paths
import pygame

pygame.init()

settings = {

    "player_type_string": image_paths["player_white"],
    "bullet_type_string": image_paths["bullet_green"],
    "cursor_type_string": image_paths["cursor_red"],

    "start_bullets": 100,
    "start_lives": 3,
    "player_speed": 6,
    "bullet_speed": 15,
    "screen_width": 1500,
    "screen_height": 1000,
    "coins": 0,
    "alien_speed": 1.5,
    "drop_probability": 10,
    "drop_frames": 600,
    "drop_lives": 1,
    "drop_bullets": 50,
    "drop_coins": 2,
    "fps": 60,
    "hud_spacing": 10,
    "font": pygame.font.Font(font_paths["arcade_classic"], 40)

}
