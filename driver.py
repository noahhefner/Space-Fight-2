"""
Noah Hefner
Space Fight 2.0
Last Edit: 7/21/2020
"""

# Imports
import os
import pygame
from nhefner_pygame_menus import MenuManager, ButtonPicture, ButtonText, Picture, Text, Page
from sf2.common.strings import image_paths
from sf2.game.game import Game
from sf2.common.settings import settings_game, settings_program

# Initialize pygame
pygame.init()

# Create screen and clock
screen = pygame.display.set_mode([settings_program["screen_width"], settings_program["screen_height"]])
clock = pygame.time.Clock()

# Font object for rendering text buttons
font_size = 40
font = pygame.font.Font(os.path.abspath("sf2/resources/font/ARCADECLASSIC.TTF"), font_size)

""" Functions for buttons -------------------------------------------------- """

def change_player_image (path):
    """
    Change the image of the player in the settings dictionary.
    """

    settings_game["player_type_string"] = path

def change_bullet_image (path):
    """
    Change the image of the bullet in the settings dictionary.
    """

    settings_game["bullet_type_string"] = path

def change_cursor_image (path):
    """
    Change the image of the cursor in the settings dictionary.
    """

    settings_game["cursor_type_string"] = path

""" Menu Management System Using nhefner_pygame_menus Module --------------- """
# Create a MenuManager object
man = MenuManager(screen, clock)

# Create some games
home = Page("home")
highscores = Page("highscores")
options = Page("options")
exit_confirm = Page("exit_confirm")

# Add the pages to the MenuManager
man.add_page(home)
man.add_page(options)
man.add_page(exit_confirm)

# Set the start page
man.set_start_page("home")

# Create elements for the pages and define their actions
# Home elements
button_play = ButtonText("PLAY", font, pos = [20, 375], background_color = [255, 0, 0])
button_play.add_action(man.exit_menu)
button_options = ButtonText("OPTIONS", font, pos = [20, 425], background_color = [255, 0, 0])
button_options.add_action(man.navigate, "options")
button_quit = ButtonText("QUIT", font, pos = [20, 475], background_color = [255, 0, 0])
button_quit.add_action(man.navigate, "exit_confirm")
picture_logo = Picture(image_paths["logo"], [20, 20])

# Options elements
button_back_op = ButtonText("BACK", font, pos = [10, 10], background_color = [255, 0, 0])
button_back_op.add_action(man.navigate, "home")
selection_box = Picture(image_paths["selection_box"], [94, 64])
button_blue_ship = ButtonPicture(image_paths["player_blue"], pos = [20, 70])
button_blue_ship.add_action(change_player_image, image_paths["player_blue"])
button_blue_ship.add_action(selection_box.set_pos, pos = [14, 64])
button_white_ship = ButtonPicture(image_paths["player_white"], pos = [100, 70])
button_white_ship.add_action(change_player_image, image_paths["player_white"])
button_white_ship.add_action(selection_box.set_pos, pos = [94, 64])
button_green_ship = ButtonPicture(image_paths["player_green"], pos = [180, 70])
button_green_ship.add_action(change_player_image, image_paths["player_green"])
button_green_ship.add_action(selection_box.set_pos, pos = [174, 64])
button_yellow_ship = ButtonPicture(image_paths["player_yellow"], pos = [260, 70])
button_yellow_ship.add_action(change_player_image, image_paths["player_yellow"])
button_yellow_ship.add_action(selection_box.set_pos, pos = [254, 64])

# Exit confirm elements
text_confirmation = Text("ARE YOU SURE ABOUT THAT", font, pos = [20, 20], background_color = [255, 0, 0])
button_yes = ButtonText("YES", font, pos = [20, 90], background_color = [255, 0, 0])
button_yes.add_action(man.kill_program)
button_no = ButtonText("NO", font, pos = [20, 160], background_color = [255, 0, 0])
button_no.add_action(man.navigate, "home")

# Add the elements to their pages
# Home elements
home.add_element(button_play)
home.add_element(button_options)
home.add_element(button_quit)
home.add_element(picture_logo)

# Options elements
options.add_element(button_back_op)
options.add_element(selection_box)
options.add_element(button_blue_ship)
options.add_element(button_white_ship)
options.add_element(button_green_ship)
options.add_element(button_yellow_ship)

# Exit elements
exit_confirm.add_element(text_confirmation)
exit_confirm.add_element(button_yes)
exit_confirm.add_element(button_no)

""" Main Program Loop ------------------------------------------------------ """
while True:

    # Do the menu stuff
    man.run()

    # Creating a game object
    game = Game(screen, clock)

    # Main game loop
    while game.update():

        game.display()

    # Delete game object
    del game
