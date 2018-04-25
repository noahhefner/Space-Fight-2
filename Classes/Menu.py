# Noah Hefner
# Space Fight 2.0
# Menu Class
# Last Edit: 1/11/2018

import math
import pygame
import time

from Explosion import Explosion
from Button import Button
from Bullet import Bullet
from Alien import Alien
from Drop import Drop
from Game import Game
from Star import Star
from Player import Player
from Settings import settings
from Array import Array
from random import *
from Functions import *

from Cursor import Cursor

pygame.init()

class Menu(object):
    """ Runs the menu portion of the program. """

    def __init__(self):
        """ Initiates menu class. """

        # Cursor sprite
        self.cursor = Cursor(settings["cursor_type_string"])
        # TODO: Add cursor upgrades

        # Sprite groups that hol1d items for each screen
        self.menu_screen_home = pygame.sprite.Group()
        self.menu_screen_upgrades = pygame.sprite.Group()
        self.menu_screen_active = pygame.sprite.Group()

        # Arrays to hold positions for items for each screen
        self.array_menu_home = Array(settings["screen_width"], \
                                     settings["screen_height"], 5, 1)
        self.array_menu_upgrades = Array(settings["screen_width"], \
                                         settings["screen_height"], 5, 4)

        """" - - Home Menu Items - - """

        """ - Buttons - """
        self.button_logo = Button("/home/noahhefner/Git/Space-Fight-2/Images/space_fight_logo.png")
        self.button_start = Button("START")
        self.button_upgrades = Button("UPGRADES")
        self.button_quit = Button("QUIT")

        """ - Add home menu items to home menu group """
        self.menu_screen_home.add(self.button_logo)
        self.menu_screen_home.add(self.button_start)
        self.menu_screen_home.add(self.button_upgrades)
        self.menu_screen_home.add(self.button_quit)

        """ - Grid home menu buttons - """
        self.button_logo.position([((1/2) * settings["screen_width"] - (1/2) * self.button_logo.rect.x), 20])
        self.button_start.position(self.array_menu_home.position(1,3))
        self.button_upgrades.position(self.array_menu_home.position(1,4))
        self.button_quit.position(self.array_menu_home.position(1,5))

        """ - - Upgrade Menu Items - - """

        """ - Buttons - """
        self.player_blue_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/player_blue.png", True)
        self.player_green_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/player_green.png", True)
        self.player_white_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/player_white.png", True)
        self.player_yellow_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/player_yellow.png", True)
        # TODO: Add purple player

        self.bullet_blue_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/bullet_blue.png", True)
        self.bullet_green_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/bullet_green.png", True)
        self.bullet_purple_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/bullet_purple.png", True)
        self.bullet_red_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/bullet_red.png", True)
        self.bullet_yellow_button = Button("/home/noahhefner/Git/Space-Fight-2/Images/bullet_yellow.png", True)

        self.boost_speed_button = Button("SPEED (10 COINS)")
        self.boost_lives_button = Button("LIVES (30 COINS)")
        self.boost_ammo_button = Button("AMMOS (20 COINS)")

        self.button_active_player = Button(settings["player_type_string"], True)
        self.button_active_bullet = Button(settings["bullet_type_string"], True)

        self.current_button = Button("CURRENT")
        self.current_player = Button(settings["player_type_string"], True)
        self.current_bullet = Button(settings["bullet_type_string"], True)
        self.back_button = Button("BACK", False, True)
        self.coin_pic_image = Button("/home/noahhefner/Git/Space-Fight-2/Images/coin.png")
        self.coin_count_image = Button(str(settings["coins"]))

        """ - Add upgrade menu items to upgrade menu group - """
        self.menu_screen_upgrades.add(self.player_blue_button)
        self.menu_screen_upgrades.add(self.player_green_button)
        self.menu_screen_upgrades.add(self.player_white_button)
        self.menu_screen_upgrades.add(self.player_yellow_button)

        self.menu_screen_upgrades.add(self.bullet_blue_button)
        self.menu_screen_upgrades.add(self.bullet_green_button)
        self.menu_screen_upgrades.add(self.bullet_purple_button)
        self.menu_screen_upgrades.add(self.bullet_red_button)
        self.menu_screen_upgrades.add(self.bullet_yellow_button)

        self.menu_screen_upgrades.add(self.boost_speed_button)
        self.menu_screen_upgrades.add(self.boost_lives_button)
        self.menu_screen_upgrades.add(self.boost_ammo_button)

        self.menu_screen_upgrades.add(self.current_button)
        self.menu_screen_upgrades.add(self.back_button)
        self.menu_screen_upgrades.add(self.current_player)
        self.menu_screen_upgrades.add(self.current_bullet)
        self.menu_screen_upgrades.add(self.coin_pic_image)
        self.menu_screen_upgrades.add(self.coin_count_image)

        """ - Grid upgrade menu buttons - """
        self.player_white_button.position(self.array_menu_upgrades.position(1,1))
        self.player_blue_button.position(self.array_menu_upgrades.position(1,2))
        self.player_green_button.position(self.array_menu_upgrades.position(1,3))
        self.player_yellow_button.position(self.array_menu_upgrades.position(1,4))

        self.bullet_blue_button.position(self.array_menu_upgrades.position(2,2))
        self.bullet_green_button.position(self.array_menu_upgrades.position(2,3))
        self.bullet_purple_button.position(self.array_menu_upgrades.position(2,5))
        self.bullet_red_button.position(self.array_menu_upgrades.position(2,1))
        self.bullet_yellow_button.position(self.array_menu_upgrades.position(2,4))

        self.boost_speed_button.position(self.array_menu_upgrades.position(3,1))
        self.boost_lives_button.position(self.array_menu_upgrades.position(3,3))
        self.boost_ammo_button.position(self.array_menu_upgrades.position(3,5))

        # Not part of grid, needs coords set manually
        self.back_button = set_coords(self.back_button, 10, 10)
        self.current_player = set_coords(self.current_player, 100, 100)

        self.set_active(self.menu_screen_home)

        return

    def process_user_events(self):
        """ Handle user input. """

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    settings["active_screen"] = "done"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                # TODO: Move cursor pos sampling to arg as clicked() method

                # If the current screen is the home screen
                if settings["active_submenu"] == "home":

                    print("YEAH")
                    if self.button_quit.is_clicked(mouse_pos):

                        settings["active_screen"] = "done"

                    elif self.button_start.is_clicked(mouse_pos):

                        settings["active_screen"] = "game"

                    elif self.button_upgrades.is_clicked(mouse_pos):

                        settings["active_submenu"] = "upgrades"

                # If the current screen is the upgrades screen
                if settings["active_submenu"] == "upgrades":

                    if self.back_button.is_clicked(mouse_pos):

                        settings["active_submenu"] = "home"

                    if self.player_white_button.is_clicked(mouse_pos):

                        settings["player_type_string"] = "player_white.png"

                    elif self.player_blue_button.is_clicked(mouse_pos):

                        settings["player_type_string"] = "player_blue.png"

                    elif self.player_green_button.is_clicked(mouse_pos):

                        settings["player_type_string"] = "player_green.png"

                    elif self.player_yellow_button.is_clicked(mouse_pos):

                        settings["player_type_string"] = "player_yellow.png"

                    elif self.bullet_red_button.is_clicked(mouse_pos):

                        settings["bullet_type_string"] = "bullet_red.png"

                    elif self.bullet_green_button.is_clicked(mouse_pos):

                        settings["bullet_type_string"] = "bullet_green.png"

                    elif self.bullet_green_button.is_clicked(mouse_pos):

                        settings["bullet_type_string"] = "bullet_purple.png"

                    elif self.bullet_yellow_button.is_clicked(mouse_pos):

                        settings["bullet_type_string"] = "bullet_yellow.png"

                    elif self.bullet_blue_button.is_clicked(mouse_pos):

                        settings["bullet_type_string"] = "bullet_blue.png"

                    elif self.boost_speed_button.is_clicked(mouse_pos) and \
                    settings["coins"] >= 10:

                        settings["player_speed"] += 3
                        settings["coins"] -= 10

                    elif self.boost_ammo_button.is_clicked(mouse_pos) and \
                    self.settings["coins"] >= 20:

                        settings["player_start_ammo"] += 50
                        settings["coins"] -= 20

                    elif self.boost_lives_button.is_clicked(mouse_pos) and \
                    settings["coins"] >= 30:

                        settings["player_start_lives"] += 1
                        settings["coins"] -= 30

        return

    def update(self):
        """ Update the Text menu items. """

        self.menu_screen_active.update()

        return

    def set_active(self, new_active):

        self.menu_screen_active.empty()

        for item in new_active:

            self.menu_screen_active.add(item)


    def display_frame(self, surface):
        """ Draw the sprites needed for the current screen.
        Args:
            surface (pygame surface): pygame surface on which the screen will be
            drawn
        """

        self.menu_screen_active.draw(surface)

        return
