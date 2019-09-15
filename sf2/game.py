"""
Noah Hefner
Space Fight 2.0
Game Backend Class
Last Edit: 8/3/2019
"""

# Imports
import pygame

from alien import Alien
from audio_player import AudioPlayer
from bullet import Bullet
from constants import WHITE, BLACK
from cursor import Cursor
from drop import Drop
from explosion import Explosion
from player import Player
from settings import settings
from star import Star
from strings import image_paths

pygame.init()  # Initialize pygame


class Game:
    """
    Handles all sprite movement, collision detection, score, etc.

    Attributes:
        aliens (pygame.sprite.Group): Sprite group of all aliens.
        bullets (pygame.sprite.Group): Sprite group of all bullets.
        drops (pygame.sprite.Group): Sprite group of all drops.
        explosions (pygame.sprite.Group): Sprite group of all explosions.
        stars (pygame.sprite.Group): Sprite group of all stars.

        cursor (Cursor): The cursor sprite.
        player (Player): The player sprite.

        audio_player (AudioPlayer): Handles all audio for the game.

        coins (int): Number of coins the player has.
        score (int): Current score the player has.
        hud (HUD): Overlay that contains information for the player.
    """

    def __init__(self, surface):
        """
        Initialize a Game object.
        """

        # Surface to blit everything to
        self.surface = surface

        # Sprite Groups
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        # Sprites
        self.cursor = Cursor(image_paths["cursor_red"])
        self.player = Player(settings["player_type_string"])
        self.bullet_image = settings["bullet_type_string"]
        for i in range(20):
            new_alien = Alien(image_paths["alien1"])
            self.aliens.add(new_alien)
        for i in range(int(settings["screen_width"] / 2)):
            new_star = Star(image_paths["star"])
            self.stars.add(new_star)

        # AudioPlayer
        self.audio_player = AudioPlayer()

        self.coins = settings["coins"]
        self.score = 0
        self.hud = Game.HUD(self.score, self.player.bullets, self.coins)

        return

    def update(self, user_events):
        """"
        Handles user input, collision detection, and updates all sprites.

        Parameters:
            user_events (pygame.event): List of user inputs.
        Returns:
            boolean: True for continue the game, False to end the game.
        """

        # Handle user input
        for event in user_events:

            if event.type == pygame.QUIT:

                # End game
                return False

            # Fire bullet when user presses left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                    self.player.bullets > 0:

                self.audio_player.play_bullet_fire()
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

        # Collision detection and repercussions
        # Bullet-Alien collision
        alien_bullet_collision = \
            pygame.sprite.groupcollide(self.aliens, self.bullets, False, True)

        for alien in alien_bullet_collision:

            self.audio_player.play_explosion()

            # Spawn an explosion and kill the alien sprite
            explosion = Explosion(alien.rect.x, alien.rect.y)
            self.explosions.add(explosion)
            self.score += 1
            alien.kill()

            # Make a new alien to take its place
            self.__update_alien_speed()
            new_alien = Alien(image_paths["alien1"])
            self.aliens.add(new_alien)

            # Spawn a drop if the alien was a carrier
            if alien.is_drop_carrier():

                drop = Drop(alien.get_x(), alien.get_y())
                self.drops.add(drop)

        # Player-Alien collision
        alien_player_collision = \
            pygame.sprite.spritecollide(self.player, self.aliens, True)

        for alien in alien_player_collision:

            self.audio_player.play_hitmarker()

            # Spawn an explosion in that area and subtract one player life
            explosion = Explosion(alien.rect.x, alien.rect.y)
            self.explosions.add(explosion)
            self.player.lives -= 1  # Function this into player class

        # Player-Drop collision
        player_drop_collision = \
            pygame.sprite.spritecollide(self.player, self.drops, True)

        for drop in player_drop_collision:

            # Perform the perks ability/benefit
            if drop.get_type() == image_paths["drop_bullets"]:

                self.audio_player.play_pickup_life()
                self.player.bullets += settings["drop_bullets"]

            elif drop.get_type() == image_paths["drop_coin"]:

                self.audio_player.play_pickup_coin()
                self.coins += 1

            elif drop.get_type() == image_paths["drop_life"]:

                self.audio_player.play_pickup_life()
                self.player.lives += 1

        # Sprite updates (call update function on everything)
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
            alien.update(self.player.rect.center)

        # Star update
        for star in self.stars:
            star.update()

        self.player.update()
        self.cursor.update(pygame.mouse.get_pos())
        self.hud.update(self.score, self.player.bullets,
                        self.coins)

        # End game if the player is out of lives
        if self.player.lives <= 0:

            return False

        # Return True if the game should continue
        return True

    def get_aliens(self):
        """
        Gets the aliens sprite group.

        Returns:
            self aliens (pygame.sprite.Group): Sprite group of aliens.
        """

        return self.aliens

    def get_bullets(self):
        """
        Gets the bullets sprite group.

        Returns:
            self.bullets (pygame.sprite.Group): Sprite group of bullets.
        """

        return self.bullets

    def get_drops(self):
        """
        Gets the drops sprite group.

        Returns:
            self.drops (pygame.sprite.Group): Sprite group of drops.
        """

        return self.drops

    def get_explosions(self):
        """
        Gets the explosions sprite group.

        Returns:
            self.explosions (pygame.sprite.Group): Sprite group of explosions.
        """

        return self.explosions

    def get_stars(self):
        """
        Gets the stars sprite group.

        Returns:
            self.stars (pygame.sprite.Group): Sprite group of stars.
        """

        return self.stars

    def set_bullet_image(self, image_string):

        self.bullet_image = image_string

        return True

    def display(self):
        """
        Draw everything to the surface.
        """

        # Fill background
        self.surface.fill(BLACK)

        # Blit stars
        self.get_stars().draw(self.surface)

        # Blit HUD
        self.surface.blit(self.hud.counter_bullets.image,
                         [self.hud.counter_bullets.rect.x,
                          self.hud.counter_bullets.rect.y])

        self.surface.blit(self.hud.counter_coins.image,
                         [self.hud.counter_coins.rect.x,
                          self.hud.counter_coins.rect.y])

        self.surface.blit(self.hud.counter_score.image,
                         [self.hud.counter_score.rect.x,
                          self.hud.counter_score.rect.y])

        for i in range(self.player.lives):

            x = (settings["hud_spacing"] * (i + 1)) + \
                (i * self.hud.heart.rect.width)
            y = settings["hud_spacing"]

            self.surface.blit(self.hud.heart.image, [x, y])

        # Blit bullets
        self.get_bullets().draw(self.surface)

        # Blit explosions
        self.get_explosions().draw(self.surface)

        # Blit drops
        self.get_drops().draw(self.surface)

        # Blit aliens
        self.get_aliens().draw(self.surface)

        # Blit player
        self.surface.blit(self.player.image,
                         [self.player.get_x(),
                          self.player.get_y()])

        # Blit cursor
        self.surface.blit(self.cursor.image,
                         [self.cursor.get_x(),
                          self.cursor.get_y()])

        return

    def reset(self, surface):

        self.__init__(surface)

        return

    def __spawn_bullet(self):
        """
        Spawns a bullet and adds it to bullet sprite list.
        """

        mouse_pos = pygame.mouse.get_pos()
        new_bullet = Bullet(self.bullet_image, mouse_pos,
                            self.player.rect.center)
        self.bullets.add(new_bullet)
        self.player.bullets -= 1

        return True

    def __update_alien_speed(self):
        """
        Increment alien speed based on player score.
        """

        settings["alien_speed"] += 0.01

        return True

    class HUD:
        """
        Visual overlay that contains player information.

        Attributes:
            heart (pygame.sprite.Sprite): Heart sprite used to blit lives.
            counter_score (pygame.sprite.Sprite): Player score counter.
            counter_bullets (pygame.sprite.Sprite): Player bullet counter.
            counter_coins (pygame.sprite.Sprite): Player coins counter.
        """

        def __init__(self, score, bullets, coins):
            """
            Initialize a HUD object.

            Parameters:
                score (int): Current score of player.
                bullets (int): Current bullet count of player.
                coins (int): Current coin count of player.
            """

            self.heart = pygame.sprite.Sprite()
            self.heart.image = \
                pygame.image.load(image_paths["heart"]).convert()
            self.heart.rect = self.heart.image.get_rect()

            self.counter_score = pygame.sprite.Sprite()
            self.counter_score.image = settings["font"].render(
                "SCORE    " + str(score), False, WHITE)
            self.counter_score.rect = self.counter_score.image.get_rect()

            self.counter_bullets = pygame.sprite.Sprite()
            self.counter_bullets.image = settings["font"].render(
                "BULLETS    " + str(bullets), False, WHITE)
            self.counter_bullets.rect = self.counter_bullets.image.get_rect()

            self.counter_coins = pygame.sprite.Sprite()
            self.counter_coins.image = settings["font"].render(
                "COINS    " + str(coins), False, WHITE)
            self.counter_coins.rect = self.counter_coins.image.get_rect()

            return

        def update(self, score, bullets, coins):
            """
            Remake counter sprites with appropriate data.

            Parameters:
                score (int): Current score of player.
                bullets (int): Current bullet count of player.
                coins (int): Current coin count of player.
            """

            # Update bullet counter
            self.counter_bullets.image = settings["font"].render(
                "BULLETS    " + str(bullets), False, WHITE)
            self.counter_bullets.rect = self.counter_bullets.image.get_rect()
            self.counter_bullets.rect.x = settings["hud_spacing"]
            self.counter_bullets.rect.y = self.heart.rect.y + \
                self.heart.rect.height + (settings["hud_spacing"] * 2)

            # Update coin counter
            self.counter_coins.image = settings["font"].render(
                "COINS    " + str(coins), False, WHITE)
            self.counter_coins.rect = self.counter_coins.image.get_rect()
            self.counter_coins.rect.x = settings["hud_spacing"]
            self.counter_coins.rect.y = self.counter_bullets.rect.y + \
                self.counter_bullets.rect.height + settings["hud_spacing"]

            # Update score counter
            self.counter_score.image = settings["font"].render(
                "SCORE    " + str(score), False, WHITE)
            self.counter_score.rect = self.counter_score.image.get_rect()
            self.counter_score.rect.x = settings["hud_spacing"]
            self.counter_score.rect.y = self.counter_coins.rect.y + \
                self.counter_coins.rect.height + settings["hud_spacing"]

            return True
