"""
Noah Hefner
Space Fight 2.0
AudioPlayer Class
Last Edit: 8/2/2019
"""

import pygame
from strings import audio_paths

pygame.init()  # Initialize pygame


class AudioPlayer:
    """
    Holds Sound objects and methods to play them.

    Attributes:
        bullet_fire (pygame.mixer.Sound): Bullet firing Sound object.
        explosion (pygame.mixer.Sound): Explosion Sound object.
        hitmarker (pygame.mixer.Sound): Alien/player collision Sound object.
        pickup_bullets (pygame.mixer.Sound): Pickup bullets Sound obejct.
        pickup_coin (pygame.mixer.Sound): Pickup coin Sound object.
        pickup_life (pygame.mixer.Sound): Pickup life Sound object.
        theme (pygame.mixer.Sound): Theme song Sound object.
    """

    def __init__(self):
        """
        Instantiate a new AudioPlayer object.
        """

        self.bullet_fire = pygame.mixer.Sound(audio_paths["bullet_fire"])
        self.explosion = pygame.mixer.Sound(audio_paths["explosion"])
        self.hitmarker = pygame.mixer.Sound(audio_paths["hitmarker"])
        self.pickup_bullets = pygame.mixer.Sound(audio_paths["pickup_bullets"])
        self.pickup_coin = pygame.mixer.Sound(audio_paths["pickup_coin"])
        self.pickup_life = pygame.mixer.Sound(audio_paths["pickup_life"])
        self.theme = pygame.mixer.Sound(audio_paths["theme"])

        return

    def play_bullet_fire(self):
        """
        Play bullet firing sound effect.
        """

        self.bullet_fire.play()

        return

    def play_explosion(self):
        """
        Play explosion sound effect.
        """

        self.explosion.play()

        return

    def play_hitmarker(self):
        """
        Play hitmarker sound effect.
        """

        self.hitmarker.play()

        return

    def play_pickup_bullets(self):
        """
        Play pickup bullets sound effect.
        """

        self.pickup_bullets.play()

        return

    def play_pickup_coin(self):
        """
        Play pickup coin sound effect.
        """

        self.pickup_coin.play()

        return

    def play_pickup_life(self):
        """
        Play pickup life sound effect.
        """

        self.pickup_life.play()

        return

    def play_theme(self):
        """
        Play theme song.
        """

        self.theme.play(-1)  # -1 plays the song on repeat

        return
