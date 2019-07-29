# Noah Hefner
# Space Fight 2.0
# Drop Class
# Last Edit: 7/28/2019

from player import Player
from bullet import Bullet
from alien import Alien
from settings import settings
from explosion import Explosion
from strings import strings
from star import Star
from drop import Drop
import pygame
from constants import WHITE

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
        self.hud = GameBackend.HUD(self.score, self.player.lives,
                                   self.player.bullets, self.coins)

        # Create stars for background
        for i in range(int(settings["screen_width"] / 2)):
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

                if event.key == pygame.K_w:

                    self.player.change_speed(0, -1 * settings["player_speed"])

                if event.key == pygame.K_a:

                    self.player.change_speed(-1 * settings["player_speed"], 0)

                if event.key == pygame.K_s:

                    self.player.change_speed(0, settings["player_speed"])

                if event.key == pygame.K_d:

                    self.player.change_speed(settings["player_speed"], 0)

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_w:

                    self.player.change_speed(0, settings["player_speed"])

                if event.key == pygame.K_a:

                    self.player.change_speed(settings["player_speed"], 0)

                if event.key == pygame.K_s:

                    self.player.change_speed(0, -1 * settings["player_speed"])

                if event.key == pygame.K_d:

                    self.player.change_speed(-1 * settings["player_speed"], 0)

        """"
        ------------------------------------------------------------------------
        COLLISION DETECTION AND COLLISION EFFECTS
        ------------------------------------------------------------------------
        """
        # Bullet-Alien collision
        alien_bullet_collision = \
            pygame.sprite.groupcollide(self.aliens, self.bullets, False, True)

        for alien in alien_bullet_collision:

            # Spawn an explosion and kill the alien sprite
            explosion = Explosion(alien.rect.x, alien.rect.y)
            self.explosions.add(explosion)
            self.score += 1
            alien.kill()

            # Make a new alien to take its place
            self.__update_alien_speed()
            new_alien = Alien(settings["image_string_alien1"])
            self.aliens.add(new_alien)

            # Spawn a drop if the alien was a carrier
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
            self.player.lives -= 1  # Function this into player class

        # Player-Drop collision
        player_drop_collision = \
            pygame.sprite.spritecollide(self.player, self.drops, True)

        for drop in player_drop_collision:

            # Perform the perks ability/benefit
            if drop.get_type() == strings["drop_bullets"]:

                self.player.bullets += settings["drop_bullets"]

            elif drop.get_type() == strings["drop_coin"]:

                self.coins += 1

            elif drop.get_type() == strings["drop_life"]:

                self.player.lives += 1

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

        # Star update
        for star in self.stars:
            star.update()

        self.player.update()
        self.hud.update(self.score, self.player.lives, self.player.bullets,
                        self.coins)

        if self.player.lives <= 0:

            return False

        return True

    def __spawn_bullet(self):
        """ Spawns a bullet. """

        mouse_pos = pygame.mouse.get_pos()
        new_bullet = Bullet(settings["bullet_type_string"], mouse_pos)
        self.bullets.add(new_bullet)
        self.player.bullets -= 1

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

        settings["alien_speed"] += 0.01

    class HUD:

        def __init__(self, score, lives, bullets, coins):

            self.hearts = []

            self.counter_score = pygame.sprite.Sprite()
            self.counter_score.image = settings["font"].render(
                "SCORE: " + str(score), False, WHITE)
            self.counter_score.rect = self.counter_score.image.get_rect()

            self.counter_bullets = pygame.sprite.Sprite()
            self.counter_bullets.image = settings["font"].render(
                "BULLETS: " + str(bullets), False, WHITE)
            self.counter_bullets.rect = self.counter_bullets.image.get_rect()

            self.counter_coins = pygame.sprite.Sprite()
            self.counter_coins.image = settings["font"].render(
                "COINS: " + str(coins), False, WHITE)
            self.counter_coins.rect = self.counter_coins.image.get_rect()

            return

        def update(self, score, lives, bullets, coins):

            # Update bullet counter
            self.counter_bullets.image = settings["font"].render(
                "BULLETS: " + str(bullets), False, WHITE)
            self.counter_bullets.rect = self.counter_bullets.image.get_rect()
            self.counter_bullets.rect.x = settings["hud_spacing"]
            self.counter_bullets.rect.y = (settings["hud_spacing"] * 2) + 100

            # Update coin counter
            self.counter_coins.image = settings["font"].render(
                "COINS: " + str(coins), False, WHITE)
            self.counter_coins.rect = self.counter_coins.image.get_rect()
            self.counter_coins.rect.x = settings["hud_spacing"]
            self.counter_coins.rect.y = (settings["hud_spacing"] * 3) + 120

            # Update score counter
            self.counter_score.image = settings["font"].render(
                "SCORE: " + str(score), False, WHITE)
            self.counter_score.rect = self.counter_score.image.get_rect()
            self.counter_score.rect.x = settings["hud_spacing"]
            self.counter_score.rect.y = (settings["hud_spacing"] * 3) + 140

            # Ensure correct number of hearts
            while len(self.hearts) != lives:

                if len(self.hearts) < lives:

                    heart = pygame.sprite.Sprite()
                    heart.image = pygame.image.load(strings["heart"])
                    heart.rect = heart.image.get_rect()
                    self.hearts.append(heart)

                else:

                    self.hearts.remove(self.hearts[len(self.hearts) - 1])

            # Ensure heart coordinates
            for i in range(len(self.hearts)):

                self.hearts[i].rect.x = (settings["hud_spacing"] * i) + \
                    (self.hearts[i].rect.width * i)
                self.hearts[i].rect.y = settings["hud_spacing"]

            return True
