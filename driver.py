"""
Noah Hefner
Space Fight 2.0
Menu Manager Usage Demo
Last Edit: 6/30/2020
"""

# Imports
import pygame
from sf2.game.game_frontend import GameFrontend  # Game

from sf2.common.settings import settings_game, settings_program  # Settings

from sf2.nhefner_pg_menus.menus import MenuManager, ButtonPicture, ButtonText, Page, Picture

stats = {

    "player_speed" : 5,
    "player_lives" : 3

}

def add_life ():

    stats["player_lives"] += 1
    print(stats["player_lives"])

# Initialize pygame
pygame.init()

# Create screen and clock
screen = pygame.display.set_mode([settings_program["screen_width"], settings_program["screen_height"]])
clock = pygame.time.Clock()

# Font object for rendering text buttons
font = pygame.font.SysFont('ArcadeClassic', 100, False, False)

# Create MenuManager
man = MenuManager(screen, clock)

# Create some pages
home = Page("home")
options = Page("options")
exit_confirm = Page("exit_confirm")

# Create some buttons
button_play = ButtonText("PLAY", font, man.exit_menu, pos = [10, 10], background_color = [255, 0, 0])
button_options = ButtonText("OPTIONS", font, man.navigate, "options", pos = [10, 100], background_color = [255, 0, 0])
button_quit = ButtonText("QUIT", font, man.navigate, "exit_confirm", pos = [10, 175], background_color = [255, 0, 0])
button_add = ButtonText("ADD", font, add_life, pos = [10, 250], background_color = [255, 0, 0])

button_yes = ButtonText("YES", font, man.kill_program, pos = [0, 0], background_color = [255, 0, 0])
button_no = ButtonText("NO", font, man.navigate, "home", pos = [0, 100], background_color = [255, 0, 0])

# Add buttons to their pages
home.add_element(button_play)
home.add_element(button_options)
home.add_element(button_quit)
home.add_element(button_add)

exit_confirm.add_element(button_yes)
exit_confirm.add_element(button_no)

# Add pages to MenuManager
man.add_page(home)
man.add_page(options)
man.add_page(exit_confirm)

# Set a start page
man.set_start_page(home)

while True:

    """ Do the menu stuff """
    man.do_menu_stuff()

    """ Game code goes here """
    game = GameFrontend(screen, clock)

    while game.update():

        game.display()

    del game
