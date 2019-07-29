# Noah Hefner
# Space Fight 2.0
# Settings Dictionary
# Last Edit: 7/25/2019

from strings import strings
import pygame

pygame.init()

settings = {

    "player_type_string": strings["player_white"],
    "bullet_type_string": strings["bullet_green"],
    "cursor_type_string": strings["cursor_red"],
    "image_string_alien1": strings["alien1"],
    "image_string_star": strings["star"],

    "start_bullets": 100,
    "start_lives": 3,
    "player_speed": 6,
    "bullet_speed": 15,
    "screen_width": 1000,
    "screen_height": 800,
    "coins": 0,
    "player_x_center": 0,
    "player_y_center": 0,
    "alien_speed": 1.5,
    "drop_probability": 10,
    "drop_frames": 600,
    "drop_lives": 1,
    "drop_bullets": 50,
    "drop_coins": 2,
    "fps": 60,
    "hud_spacing": 10,
    "font": pygame.font.SysFont('04B_30_', 20, False, False)

}
