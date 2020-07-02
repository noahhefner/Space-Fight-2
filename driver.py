"""
Noah Hefner
Space Fight 2.0
Menu Manager Usage Demo
Last Edit: 7/2/2020
"""

# Imports
import pygame
from sf2.game.game_frontend import GameFrontend
from sf2.common.settings import settings_game, settings_program
from sf2.nhefner_pg_menus.menus import MenuManager, ButtonPicture, ButtonText, Page, Picture

# Initialize pygame
pygame.init()

# Create screen and clock
screen = pygame.display.set_mode([settings_program["screen_width"], settings_program["screen_height"]])
clock = pygame.time.Clock()

# Font object for rendering text buttons
font = settings_game["font"]

""" -------------------------- Create MenuManager -------------------------- """
man = MenuManager(screen, clock)

""" --------------------------- Create Some Pages -------------------------- """
home = Page("home")
highscores = Page("highscores")
options = Page("options")
exit_confirm = Page("exit_confirm")

""" ------------------------ Add Pages to MenuManager ---------------------- """
man.add_page(home)
man.add_page(highscores)
man.add_page(options)
man.add_page(exit_confirm)

""" ---------------------------- Set a Start Page -------------------------- """
man.set_start_page(home)

""" -------------------------- Create Some Buttons ------------------------- """
# Home buttons
button_play = ButtonText("PLAY", font, man.exit_menu, pos = [10, 10], background_color = [255, 0, 0])
button_highscores = ButtonText("HIGHSCORES", font, man.navigate, "highscores", pos = [10, 60], background_color = [255, 0, 0])
button_options = ButtonText("OPTIONS", font, man.navigate, "options", pos = [10, 110], background_color = [255, 0, 0])
button_quit = ButtonText("QUIT", font, man.navigate, "exit_confirm", pos = [10, 160], background_color = [255, 0, 0])

# Highscores buttons
button_back_hs = ButtonText("BACK", font, man.navigate, "home", pos = [10, 10], background_color = [255, 0, 0])

# Options buttons
button_back_op = ButtonText("BACK", font, man.navigate, "home", pos = [10, 10], background_color = [255, 0, 0])

# Exit confirm buttons
button_yes = ButtonText("YES", font, man.kill_program, pos = [0, 0], background_color = [255, 0, 0])
button_no = ButtonText("NO", font, man.navigate, "home", pos = [0, 100], background_color = [255, 0, 0])

""" ----------------------- Add Buttons to Their Pages --------------------- """
# Home buttons
home.add_element(button_play)
home.add_element(button_highscores)
home.add_element(button_options)
home.add_element(button_quit)

# Highscores buttons
highscores.add_element(button_back_hs)

# Options buttons
options.add_element(button_back_op)

# Exit confirm buttons
exit_confirm.add_element(button_yes)
exit_confirm.add_element(button_no)

""" --------------------------- Main Program Loop -------------------------- """
while True:

    """ Do the menu stuff """
    man.do_menu_stuff()

    """ Game code goes here """
    game = GameFrontend(screen, clock)

    while game.update():

        game.display()

    del game

    """ Highscore save """
