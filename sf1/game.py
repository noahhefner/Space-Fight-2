# Noah Hefner
# Space Fight 2.0
# Game Class
# Last Edit: 4/25/2018

import math
import pygame
import time

from Functions import *
from Explosion import Explosion
from Button import Button
from Bullet import Bullet
from Alien import Alien
from Drop import Drop
from Cursor import Cursor
from Star import Star
from Player import Player
from Settings import settings
from Array import Array
from random import *

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

pygame.init()

class Game(object):
    """ Holds code regarding in-game elements. """

    def __init__(self):
        """ Initiates game class.

        Args:
            settings (list): list of settings from menu [type_player_string,
            type_bullet_string, player_speed]
        """

        self.score = 0
        self.paused = False

        # Load player, bullet, and cursor settings
        self.type_player_string = settings["player_type_string"]
        self.type_bullet_string = settings["bullet_type_string"]
        self.type_cursor_string = settings["cursor_type_string"]

        # Create player and cursor with those settings
        self.player = Player(self.type_player_string)
        self.cursor = Cursor(self.type_cursor_string)

        # Load starting bullets count settings, start live settings, player
        # speed settings
        self.bullet_amount = settings["start_ammo"]
        self.lives = settings["start_lives"]
        self.player.speed = settings["start_speed"]

        self.time = time.clock()

        # Create the groups to hold game items
        self.bullets = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])
        self.aliens = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])
        self.explosions = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])
        self.drops = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])
        self.hud = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])

        string_score_counter = "SCORE: " + str(self.score)
        string_ammo_counter = "BULLETS: " + str(self.bullet_amount)

        self.bullet_counter = Button(string_ammo_counter)
        self.score_counter = Button(string_score_counter)

        self.bullet_counter.scale = .25
        self.score_counter.scale = .25

        self.hud.add(self.bullet_counter)
        self.hud.add(self.score_counter)

        self.score_counter.rect.y = 10
        self.score_counter.rect.x = 10
        self.bullet_counter.rect.y = self.score_counter.rect.y + self.score_counter.rect.height + 10
        self.bullet_counter.rect.x = 10

        # Make cursor invisible
        pygame.mouse.set_visible(False)

        self.heart_image = pygame.image.load("/home/noahhefner/Git/Space-Fight-2/Images/heart.png").convert()

        return

    def draw_lives(self, surface):
        """ Draw he players live count in hearts. """

        x_coord = settings["screen_width"] - 100
        y_coord = 10

        for i in range(self.lives):

            surface.blit(self.heart_image, [x_coord - ((i + 1) * 100), y_coord])

        return

    def update_hud(self):
        """ Update the items in the hud. """

        self.hud.empty()

        string_score_counter = "SCORE: " + str(self.score)
        string_live_counter = "LIVES: " + str(self.lives)
        string_ammo_counter = "BULLETS: " + str(self.bullet_amount)

        self.bullet_counter = Button(string_ammo_counter)
        self.live_counter = Button(string_live_counter)
        self.score_counter = Button(string_score_counter)

        self.bullet_counter.scale = .25
        self.score_counter.scale = .25

        self.score_counter.rect.y = 10
        self.score_counter.rect.x = 10
        self.live_counter.rect.y = self.score_counter.rect.y + self.score_counter.rect.height + 10
        self.live_counter.rect.x = 10
        self.bullet_counter.rect.y = self.live_counter.rect.y + self.live_counter.rect.height + 10
        self.bullet_counter.rect.x = 10

        self.hud.add(self.bullet_counter)
        self.hud.add(self.live_counter)
        self.hud.add(self.score_counter)

    def run_game_logic(self):
        """ Handles game logic. """

        if self.lives <= 0:

            settings["active_screen"] = "menu"
            return True

        # While the game is not paused
        if not self.paused:

            # Keep the number of aliens at a constant 20
            if len(self.aliens) < 20:

                alien = Alien()
                self.aliens.add(alien)

            # First, lets update everything
            self.player.update()
            self.bullets.update()
            self.aliens.update()
            self.explosions.update()
            self.drops.update()
            self.cursor.update()
            self.update_hud()

            # Get goup of aliens and bullets that collide
            alien_bullet_collision = pygame.sprite.groupcollide(self.aliens, self.bullets, False, True)

            for alien in alien_bullet_collision:

                    # Spawn an explosion in that area
                    explosion = Explosion(alien.rect.x, alien.rect.y)
                    self.explosions.add(explosion)
                    self.score += 1
                    alien.kill()

                    # Make a new alien to take its place
                    new_alien = Alien()
                    self.aliens.add(new_alien)

                    # Drop the perk if the alien was a perk carrier
                    if alien.drop <= 2:

                        drop = Drop(alien)
                        self.drops.add(drop)

            # Get group of player and aliens that collide
            alien_player_collision = pygame.sprite.spritecollide(self.player, self.aliens,
            True)

            for alien in alien_player_collision:

                # Spawn an explosion in that area and subtract one player life
                explosion = Explosion(alien.rect.x, alien.rect.y)
                self.explosions.add(explosion)
                self.lives -= 1

            # Get group of player and drops that collide
            player_drop_collision = pygame.sprite.spritecollide(self.player, self.drops,
            True)

            for drop in player_drop_collision:

                # Perform the perks ability/benefit
                if drop.image_number == 0:

                    self.bullet_amount += 50

                elif drop.image_number == 1:

                    settings["coins"] += 1

                elif drop.image_number == 2:

                    self.lives += 1

        return False

            # TODO: spawn aliens on increasingly fast time-based interval

    def spawn_bullet(self):
        """ Spawns a bullet if there are bullets left. """

        bullet = Bullet(self.type_bullet_string)
        self.bullets.add(bullet)
        self.bullet_amount -= 1

        return

    def process_user_events(self):
        """ Process user imput. """

        for event in pygame.event.get():

            # Shoot a bullet with left mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
            self.bullet_amount > 0:

                self.spawn_bullet()

            if event.type == pygame.KEYDOWN:

                # WASD for up down left right
                if event.key == pygame.K_w:

                    self.player.change_speed(0, -1 * self.player.speed)

                elif event.key == pygame.K_a:

                    self.player.change_speed(-1 * self.player.speed, 0)

                elif event.key == pygame.K_s:

                    self.player.change_speed(0, self.player.speed)

                elif event.key == pygame.K_d:

                    self.player.change_speed(self.player.speed, 0)

                # Escape to kill the program
                elif event.key == pygame.K_ESCAPE:

                    settings["active_screen"] = "done"

                # P to pause, p again to un-pause
                elif event.key == pygame.K_p:

                    if self.paused:

                        self.paused = False

                    else:

                        self.paused = True

            if event.type == pygame.KEYUP:

                # Stop movement when key is released
                if event.key == pygame.K_w:

                    self.player.change_speed(0, self.player.speed)

                elif event.key == pygame.K_a:

                    self.player.change_speed(self.player.speed, 0)

                elif event.key == pygame.K_s:

                    self.player.change_speed(0, -1 * self.player.speed)

                elif event.key == pygame.K_d:

                    self.player.change_speed(-1 * self.player.speed, 0)

        return

    def display_frame(self, surface):
        """ Draw the appropriate sprites for the current screen. """

        # Draw hud items
        for item in self.hud:

            draw_sprite(item, surface)

        # Draw player lives
        self.draw_lives(surface)

        # Draw drops, if any
        for drop in self.drops:

            draw_sprite(drop, surface)

        # Draw aliens, if any
        for alien in self.aliens:

            draw_sprite(alien, surface)

        # Draw bullets, if any
        for bullet in self.bullets:

            draw_sprite(bullet, surface)

        # Draw explosions, if any
        for explosion in self.explosions:

            draw_sprite(explosion, surface)

        # Draw player
        draw_sprite(self.player, surface)

        # Draw cursor
        draw_sprite(self.cursor, surface)

        return
