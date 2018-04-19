# Noah Hefner
# Space Fight 2.0
# Game Class
# Last Edit: 1/2/2017

import math
import pygame
import time

from Functions import *
from Explosion import Explosion
from Button import Button
from Bullet import Bullet
from Alien import Alien
from Drop import Drop
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

        self.bullets_left = 100
        self.score = 0
        self.lives = settings["player_start_lives"]
        self.paused = False
        self.type_player_string = settings["player_type_string"]
        self.type_bullet_string = settings["bullet_type_string"]
        self.player = Player(self.type_player_string)
        self.player.speed = settings["player_speed"]
        self.time = time.clock()

        self.bullets = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])
        self.aliens = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])
        self.explosions = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])

    def game_logic(self):
        """ Handles game logic. """

        if not self.paused:

            # First, lets update everything
            self.player.update()
            self.bullets.update()
            self.aliens.update()
            self.explosions.update()

            # Then see what happened
            alien_bullet_collision = pygame.groupcollide(self.aliens, self.bullets,
            False, True)

            for alien in alien_bullet_collision:

                    explosion = explosion(alien.rect.x, alien.rect.y)
                    self.score += 1

                    if alien.drop <= 3:

                        drop = Drop(alien)

            alien_player_collision = pygame.spritecollide(self.player, self.aliens,
            False)

            for alien in alien_player_collision:

                explosion = Explosion(alien.rect.x, alien.rect.y)
                self.explosions.append(explosion)
                self.lives -= 1

            # TODO: spawn aliens on increasingly fast time-based interval

    def spawn_bullet(self):
        """ Spawns a bullet if there are bullets left. """

        bullet = Bullet(self.type_bullet_string)
        bullet.set_vel()
        game.bullets.add(bullet)
        game.bullets_left -= 1

    def process_user_events(self):
        """ Process user imput. """

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
            self.bullets_left > 0:

                spawn_bullet()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:

                    self.player.change_speed(0, -1 * self.player.speed)

                elif event.key == pygame.K_a:

                    self.player.change_speed(-1 * self.player.speed, 0)

                elif event.key == pygame.K_s:

                    self.player.change_speed(0, self.player.speed)

                elif event.key == pygame.K_d:

                    self.player.change_speed(self.player.speed, 0)

                elif event.key == pygame.K_ESC:

                    self.paused = True

                else:

                    pass

    def display_frame(self, surface):
        """ Draw the appropriate sprites for the current screen. """

        for alien in self.aliens:

            draw_sprite(alien, surface)

        for bullet in self.bullets:

            draw_sprite(bullet, surface)

        for explosion in self.explosions:

            draw_sprite(explosion, surface)

        Functions.draw_sprite(self.player, surface)
