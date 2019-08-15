"""
Noah Hefner
Space Fight 2.0
Menu Manager Visualization
Last Edit: 8/15/2019
"""

import pygame
from menu_page import MenuPage
from menu_manager import MenuManager
from text_button import TextButton
from image_button import ImageButton

pygame.init()

# Some variables we will use to test
player_speed = 3
player_bullets = 50
player_lives = 3

def increase_player_speed(speed):

    speed += 1
    return

def increase_player_bullets(bullets):

    bullets += 25
    return

def add_life(lives):

    lives += 1
    return

font = pygame.font.SysFont('04B_30_', 50, False, False)

# STEP 1: Create a MenuManager
sf_menus = MenuManager()

# STEP 2: Create some pages
page_home = MenuPage("home")
page_upgrades = MenuPage("upgrades")
page_settings = MenuPage("settings")
page_customize = MenuPage("customization")

# STEP 3: Add Pages to the MenuManager
sf_menus.add_menu_page(page_home)
sf_menus.add_menu_page(page_upgrades)
sf_menus.add_menu_page(page_settings)
sf_menus.add_menu_page(page_customize)

sf_menus.go_to("home")  # Set the starting page to the home page

# STEP 4: Create buttons and add them to the pages you just created
# Create Home Page Buttons
button_play = TextButton(font, "PLAY")
button_upgrades = TextButton(font, "UPGRADES", sf_menus.go_to("upgrades"))
button_settings = TextButton(font, "SETTINGS", sf_menus.go_to("settings"))
button_customize = TextButton(font, "CUSTOMIZATION", sf_menus.go_to("customization"))
# Add them to the Home Page
page_home.add_button(button_play)
page_home.add_button(button_upgrades)
page_home.add_button(button_settings)
page_home.add_button(button_customize)

# Create Upgrades Page Buttons
button_speed = TextButton(font, "+SPEED (-10 Coins)", increase_player_speed(player_speed))
button_ammo = TextButton(font, "+AMMO (-20 Coins)", increase_player_bullets(player_bullets))
button_lives = TextButton(font, "+LIFE (-30 Coins)", add_life(player_lives))
button_back1 = TextButton(font, "BACK", sf_menus.go_to("home"))
# Add them to the Upgrades Page
page_upgrades.add_button(button_speed)
page_upgrades.add_button(button_ammo)
page_upgrades.add_button(button_lives)
page_upgrades.add_button(button_back1)

# Create Settings Page Buttons
button_mute = TextButton(font, "MUTE")
button_back2 = TextButton(font, "BACK")
# Add them to the Settings Page
page_settings.add_button(button_mute)
page_settings.add_button(button_back2)

# Create Customization Page Buttons
button_player_white  = ImageButton("player_white.png")
button_player_yellow = ImageButton("player_yellow.png")
button_player_green  = ImageButton("player_green.png")
button_player_blue   = ImageButton("player_blue.png")
button_bullet_red    = ImageButton("bullet_red.png")
button_bullet_blue   = ImageButton("bullet_blue.png")
button_bullet_green  = ImageButton("bullet_green.png")
button_bullet_purple = ImageButton("bullet_purple.png")
button_back3         = TextButton("BACK")
# Add them to the Customization Page
page_customize.add_button(button_player_white)
page_customize.add_button(button_player_yellow)
page_customize.add_button(button_player_green)
page_customize.add_button(button_player_blue)
page_customize.add_button(button_bullet_red)
page_customize.add_button(button_bullet_blue)
page_customize.add_button(button_bullet_green)
page_customize.add_button(button_bullet_purple)
page_customize.add_button(button_back3)

size = [800, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Menu Demo")

done = False
clock = pygame.time.Clock()

# Main Program Loop
while not done:

    for event in pygame.event.get():

        sf_menus.update(event)

        if event.type == pygame.QUIT:

            done = True

    sf_menus.display(screen)

    clock.tick(60)
    pygame.display.flip()