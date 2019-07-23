# Noah Hefner
# Space Fight 2.0
# Settings Dictionary
# Last Edit: 7/21/2019

import os

settings = {
    "player_type_string" : os.path.abspath("resources/images/player_white.png"),
    "bullet_type_string" : os.path.abspath("resources/images/bullet_green.png"),
    "cursor_type_string" : os.path.abspath("resources/images/cursor_red.png"),
    "image_string_alien1" : os.path.abspath("resources/images/alien_level_one.png"),
    "image_string_star" : os.path.abspath("resources/images/star.png"),
    "start_ammo" : 100,
    "start_lives" : 3,
    "player_speed" : 5,
    "bullet_speed" : 15,
    "screen_width" : 1920,
    "screen_height" : 1080,
    "coins" : 0,
    "player_x_center" : 0,
    "player_y_center" : 0,
    "alien_speed" : 2,
    "drop_probability" : 10,
    "drop_frames" : 600,
    "drop_lives" : 1,
    "drop_bullets" : 50,
    "drop_coins" : 2
}
