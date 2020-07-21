"""
Noah Hefner
Space Fight 2.0
Strings Dictionary
Last Edit: 6/30/2020
"""

# Imports
import os

# Folder paths within resources
images_folder = "sf2/resources/images/"
audio_folder = "sf2/resources/audio/"

# Image paths stored as strings
image_paths = {

    "alien1": os.path.abspath(images_folder + "alien_level_one.png"),
    "alien2": os.path.abspath(images_folder + "alien_level_two.png"),
    "alien3": os.path.abspath(images_folder + "alien_level_three.png"),
    "bullet_blue": os.path.abspath(images_folder + "bullet_blue.png"),
    "bullet_green": os.path.abspath(images_folder + "bullet_green.png"),
    "bullet_red": os.path.abspath(images_folder + "bullet_purple.png"),
    "bullet_yellow": os.path.abspath(images_folder + "bullet_yellow.png"),
    "button_options": os.path.abspath(images_folder + "button_options.png"),
    "button_quit": os.path.abspath(images_folder + "button_quit.png"),
    "button_play": os.path.abspath(images_folder + "button_play.png"),
    "button_yes": os.path.abspath(images_folder + "button_yes.png"),
    "button_you_sure": os.path.abspath(images_folder + "yousure.png"),
    "button_no": os.path.abspath(images_folder + "button_no.png"),
    "coin": os.path.abspath(images_folder + "coin.png"),
    "cursor_red": os.path.abspath(images_folder + "cursor_red.png"),
    "drop_bullets": os.path.abspath(images_folder + "drop_bullets.png"),
    "drop_coin": os.path.abspath(images_folder + "drop_coin.png"),
    "drop_life": os.path.abspath(images_folder + "drop_life.png"),
    "e1": os.path.abspath(images_folder + "e1.png"),
    "e2": os.path.abspath(images_folder + "e2.png"),
    "e3": os.path.abspath(images_folder + "e3.png"),
    "e4": os.path.abspath(images_folder + "e4.png"),
    "e5": os.path.abspath(images_folder + "e5.png"),
    "heart": os.path.abspath(images_folder + "drop_life.png"),
    "player_blue": os.path.abspath(images_folder + "player_blue.png"),
    "player_green": os.path.abspath(images_folder + "player_green.png"),
    "player_white": os.path.abspath(images_folder + "player_white.png"),
    "player_yellow": os.path.abspath(images_folder + "player_yellow.png"),
    "logo": os.path.abspath(images_folder + "space_fight_logo.png"),
    "selection_box" : os.path.abspath(images_folder + "selection_box.png"),
    "star": os.path.abspath(images_folder + "star.png")

}

# Audio paths stored as strings
audio_paths = {

    "bullet_fire": os.path.abspath(audio_folder + "bullet_fire.ogg"),
    "explosion": os.path.abspath(audio_folder + "explosion.ogg"),
    "hitmarker": os.path.abspath(audio_folder + "hitmarker.ogg"),
    "pickup_bullets": os.path.abspath(audio_folder + "pickup_bullets.ogg"),
    "pickup_coin": os.path.abspath(audio_folder + "pickup_coin.ogg"),
    "pickup_life": os.path.abspath(audio_folder + "pickup_life.ogg"),
    "theme": os.path.abspath(audio_folder + "theme.ogg")

}
