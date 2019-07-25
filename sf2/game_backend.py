# Noah Hefner
# Space Fight 2.0
# GameBackend Class
# Last Edit: 7/23/2019

# Imports
from player import Player
from bullet import Bullet
from alien import Alien
from settings import settings
from explosion import Explosion
from star import Star
import math
from drop import Drop
import pygame

pygame.init()


class GameBackend:

    def __init__(self):
        self.player = Player(settings["player_type_string"])

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.LayeredUpdates([pygame.sprite.Group()])
        self.explosions = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.score = 0
        self.lives = settings["start_lives"]
        self.coins = settings["coins"]

        # Create stars for background
        for i in range(settings["screen_width"]):
            new_star = Star(settings["image_string_star"])
            self.stars.add(new_star)

        # Make the aliens
        for i in range(20):

            new_alien = Alien(settings["image_string_alien1"])
            self.aliens.add(new_alien)

    def update(self, user_events):
        """"
        ------------------------------------------------------------------------
        HANDLE USER INPUT
        ------------------------------------------------------------------------
        """
        for event in user_events:

            if event.type == pygame.QUIT:

                # End game
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                    self.player.bullets > 0:

                self.__spawn_bullet()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    return False  # Kill switch

                elif event.key == pygame.K_w:

                    self.player.move(0, -1 * settings["player_speed"])

                elif event.key == pygame.K_a:

                    self.player.move(settings["player_speed"], 0)

                elif event.key == pygame.K_s:

                    self.player.move(0, settings["player_speed"])

                elif event.key == pygame.K_d:

                    self.player.move(settings["player_speed"], 0)

        """"
        ------------------------------------------------------------------------
        COLLISION DETECTION AND COLLISION EFFECTS
        ------------------------------------------------------------------------
        """
        # Bullet-Alien collision
        alien_bullet_collision = \
            pygame.sprite.groupcollide(self.aliens, self.bullets, False, True)

        for alien in alien_bullet_collision:

            # Spawn an explosion in that area
            explosion = Explosion(alien.rect.x, alien.rect.y)
            self.explosions.add(explosion)
            self.score += 1
            alien.kill()

            # Make a new alien to take its place
            self.__update_alien_speed()
            new_alien = Alien(settings["image_string_alien1"])
            self.aliens.add(new_alien)

            # Spawn drop if the alien was a carrier
            if alien.is_drop_carrier():

                drop = Drop(alien.get_x(), alien.get_y())
                self.drops.add(drop)

        # Player-Alien collision
        alien_player_collision = \
            pygame.sprite.spritecollide(self.player, self.aliens, True)

        for alien in alien_player_collision:

            # Spawn an explosion in that area and subtract one player life
            explosion = Explosion(alien.rect.x, alien.rect.y)
            self.explosions.add(explosion)
            self.lives -= 1

        # Player-Drop collision
        player_drop_collision = \
            pygame.sprite.spritecollide(self.player, self.drops, True)

        for drop in player_drop_collision:

            # Perform the perks ability/benefit
            if drop.image_number == 0:

                self.player.bullets += settings["drop_bullets"]

            elif drop.image_number == 1:

                settings["coins"] += 1

            elif drop.image_number == 2:

                self.lives += 1

        """"
        ------------------------------------------------------------------------
        UPDATES
        ------------------------------------------------------------------------
        """
        # Explosion update
        for explosion in self.explosions:
            explosion.update()

        # Drop update
        for drop in self.drops:
            drop.update()

        # Bullet update
        for bullet in self.bullets:
            bullet.update()

        # Alien update
        for alien in self.aliens:
            alien.update()

        if self.player.lives <= 0:

            return False

        return True

    # TODO: move this method to bullet class
    def __spawn_bullet(self):
        """ Spawns a bullet if there are bullets left. """

        mouse_pos = pygame.mouse.get_pos()

        angle = math.atan2(self.player.rect.center[1] - mouse_pos[0],
                           self.player.rect.center[0] - mouse_pos[1])

        x_traj = math.cos(angle) * settings["bullet_speed"] * -1
        y_traj = math.sin(angle) * settings["bullet_speed"] * -1

        new_bullet = Bullet(settings["bullet_type_string"], x_traj, y_traj)
        self.bullets.add(new_bullet)
        self.bullet_amount -= 1

        return

    def get_stars(self):

        return self.stars

    def get_bullets(self):

        return self.bullets

    def get_explosions(self):

        return self.explosions

    def get_drops(self):

        return self.drops

    def get_aliens(self):

        return self.aliens

    def __update_alien_speed(self):

        settings["alien_speed"] += 0.05

    def __find_player_image(self):
        return "player image"

    def __find_bullet_image(self):

        return "bullet image"

    def __find_lvl_1_alien_image(self):

        return "alien level 1 image"

    def __find_lvl_2_alien_image(self):
        return "alien level 2 image"

    def __find_lvl_3_alien_image(self):
        return "alien level 3 image"

    def __make_bullet(self):

        bullet = Bullet(self.__find_bullet_image())
        self.bullets.append(bullet)

    def __make_alien(self, image_string):

        return Alien(image_string)
