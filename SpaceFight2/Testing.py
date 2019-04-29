"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from MenuManager import MenuManager
import Constants
from MenuPage import MenuPage
from TextButton import TextButton

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

page_home = MenuPage("HOME")
# Home buttons
button_play = TextButton("PLAY", "GAME")
button_upgrades = TextButton("UPGRADES", "UPGRADES")
button_highscores = TextButton("HIGHSCORES", "HIGHSCORES")
button_quit = TextButton("QUIT", "QUIT")

page_home.add_text_button(button_play)
page_home.add_text_button(button_upgrades)
page_home.add_text_button(button_highscores)
page_home.add_text_button(button_quit)

page_upgrades = MenuPage("UPGRADES")
# Upgrades buttons
button_speed = TextButton("+SPEED (-10 Coins)", None)
button_ammo = TextButton("+AMMO (-20 Coins)", None)
button_lives = TextButton("+LIFE (-30 Coins)", None)
button_back = TextButton("BACK", "HOME")

page_upgrades.add_text_button(button_speed)
page_upgrades.add_text_button(button_ammo)
page_upgrades.add_text_button(button_lives)
page_upgrades.add_text_button(button_back)

page_highscores = MenuPage("HIGHSCORES")
# Highscores buttons
button_back = TextButton("BACK", "HOME")
# Read highscores from text file and use a loop to create ten buttons with Args
# name as the persons name and None as the to_page. Use another loop to add
# the buttons to the page.
page_highscores.add_text_button(button_back)

sf_menus = MenuManager(page_home)
sf_menus.add_menu_page(page_home)
sf_menus.add_menu_page(page_upgrades)
sf_menus.add_menu_page(page_highscores)

page_home.set_x_positioning("left")
page_home.set_y_positioning("bot")

page_upgrades.set_x_positioning("mid")
page_upgrades.set_y_positioning("mid")

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    out = sf_menus.update(event)

    if out == "GAME":

        # PLay the game here
        pass

    elif out == "QUIT":

        done = True

    sf_menus.display(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
