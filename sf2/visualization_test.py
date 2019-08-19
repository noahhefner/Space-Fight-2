"""
Noah Hefner
Space Fight 2.0
Menu Manager Visualization
Last Edit: 8/16/2019
"""

# Imports
import pygame
from menu_page import MenuPage
from menu_manager import MenuManager
from text_button import TextButton
from image_button import ImageButton
from game import Game
from strings import image_paths
from settings import settings

pygame.init()  # Initialize pygame

# Setup screen (window) and pygame Clock
size = [settings["screen_width"], settings["screen_height"]]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Menu Demo")
clock = pygame.time.Clock()

font = pygame.font.SysFont('04B_30_', 50, False, False)  # Font for menu

game = Game(screen)  # Create a game object
game.audio_player.play_theme()  # Play the theme song

# STEP 1: Create a MenuManager
sf_menus = MenuManager(screen)

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
button_play = TextButton(font, "PLAY", [sf_menus.exit_menus, game.reset], [[], [screen]])
button_upgrades = TextButton(font, "UPGRADES", [sf_menus.go_to], [["upgrades"]])
button_settings = TextButton(font, "SETTINGS", [sf_menus.go_to], [["settings"]])
button_customize = TextButton(font, "CUSTOMIZATION", [sf_menus.go_to], [["customization"]])
# Add them to the Home Page
page_home.add_button(button_play)
page_home.add_button(button_upgrades)
page_home.add_button(button_settings)
page_home.add_button(button_customize)
# Set button positioning for the home page
page_home.set_x_positioning("mid")
page_home.set_y_positioning("mid")

# Create Upgrades Page Buttons
button_speed = TextButton(font, "+SPEED (-10 Coins)")
button_ammo = TextButton(font, "+AMMO (-20 Coins)")
button_lives = TextButton(font, "+LIFE (-30 Coins)")
button_back1 = TextButton(font, "BACK", [sf_menus.go_to], [["home"]])
# Add them to the Upgra eedes Page
page_upgrades.add_button(button_speed)
page_upgrades.add_button(button_ammo)
page_upgrades.add_button(button_lives)
page_upgrades.add_button(button_back1)

# Create Settings Page Buttons
button_mute = TextButton(font, "MUTE")  # The function that goes here needs to return True
button_back2 = TextButton(font, "BACK", [sf_menus.go_to], [["home"]])
# Add them to the Settings Page
page_settings.add_button(button_mute)
page_settings.add_button(button_back2)

# Create Customization Page Buttons
button_player_white  = ImageButton("player_white.png")
button_player_yellow = ImageButton("player_yellow.png")
button_player_green  = ImageButton("player_green.png")  
button_player_blue   = ImageButton("player_blue.png", [game.player.set_image], [[image_paths["player_blue"]]])  
button_bullet_red    = ImageButton("bullet_red.png") 
button_bullet_blue   = ImageButton("bullet_blue.png")
button_bullet_green  = ImageButton("bullet_green.png")
button_bullet_purple = ImageButton("bullet_purple.png") 
button_back3         = TextButton(font, "BACK", [sf_menus.go_to], [["home"]])
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

done = False

# Main Program Loop
while not done:

    user_events = pygame.event.get()

    screen.fill([0, 0, 0])

    if sf_menus.in_menus:

        sf_menus.update(user_events)
        sf_menus.display()

    else:

        continue_playing = game.update(user_events)

        game.display()

        if not continue_playing:

            sf_menus.enter_menus()

    for event in user_events:

        if event.type == pygame.QUIT:

            done = True

    clock.tick(60)
    pygame.display.flip()

pygame.quit()