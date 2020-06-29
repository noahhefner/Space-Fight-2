"""
Noah Hefner
Space Fight 2.0
Menu Manager Usage Demo
Last Edit: 6/29/2020
"""

# Imports
import pygame
from button import Button
from game_frontend import GameFrontend
from menu_manager import MenuManager
from page import Page
from picture import Picture
from settings import settings
from strings import image_paths

# Initialize pygame
pygame.init()

# Create screen and clock
screen = pygame.display.set_mode([settings["screen_width"], settings["screen_height"]])
clock = pygame.time.Clock()

# Create MenuManager
man = MenuManager(screen, clock)

# Create some pages
home = Page("home")
options = Page("options")
exit_confirm = Page("exit_confirm")

# Create some buttons
button_play = Button(image_paths["button_play"], man.exit_menu, pos = [10, 10])
button_options = Button(image_paths["button_options"], man.navigate, "options", pos = [10, 100])
button_quit = Button(image_paths["button_quit"], man.navigate, "exit_confirm", pos = [10, 175])

picture_you_sure = Picture(image_paths["button_you_sure"], pos = [0,0])
button_yes = Button(image_paths["button_yes"], man.kill_program, pos = [10, 300])
button_no = Button(image_paths["button_no"], man.navigate, "home", pos = [50, 300])

# Add buttons to their pages
home.add_element(button_play)
home.add_element(button_options)
home.add_element(button_quit)

exit_confirm.add_element(picture_you_sure)
exit_confirm.add_element(button_yes)
exit_confirm.add_element(button_no)

# Add pages to MenuManager
man.add_page(home)
man.add_page(options)
man.add_page(exit_confirm)

# Set a start page
man.set_start_page(home)

program_running = True
menu_pregame = True
in_game = False
menu_postgame = False

while program_running:

    while menu_pregame:

        menu_pregame = man.update()
        man.display()

    in_game = True
    game = GameFrontend(screen, clock)

    while in_game:

        in_game = game.update()
        game.display()

    menu_pregame = True
