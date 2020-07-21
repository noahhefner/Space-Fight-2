"""
Noah Hefner
Space Fight 2.0
Menu Manager Usage Demo
Last Edit: 7/2/2020
"""

# Imports
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
font = settings_game["font"]

"""
Functions for buttons.
"""
def change_player_image (path):

    settings_game["player_type_string"] = path

def change_bullet_image (path):

    settings_game["bullet_type_string"] = path

def change_cursor_image (path):

    settings_game["cursor_type_string"] = path

""" -------------------------- Create MenuManager -------------------------- """
man = MenuManager(screen, clock)

""" --------------------------- Create Some Pages -------------------------- """
home = Page("home")
highscores = Page("highscores")
options = Page("options")
exit_confirm = Page("exit_confirm")

""" ------------------------ Add Pages to MenuManager ---------------------- """
man.add_page(home)
man.add_page(options)
man.add_page(exit_confirm)

""" ---------------------------- Set a Start Page -------------------------- """
man.set_start_page(home)

""" ------------------------- Create Some Elements ------------------------- """
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

""" ---------------------- Add Elements to Their Pages --------------------- """
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

""" --------------------------- Main Program Loop -------------------------- """
while True:

    """ Do the menu stuff """
    man.do_menu_stuff()

    """ Game code goes here """
    game = Game(screen, clock)

    while game.update():

        game.display()

    del game
