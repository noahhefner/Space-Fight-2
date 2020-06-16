"""
Noah Hefner
Space Fight 2.0
AudioPlayer Class
Last Edit: 6/16/2020
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

    def play_sound (self, audio_file_name, repeat = False):
        """
        Plays an audio clip.

        Arguments:
            audio_file_name: Name of audio file. Must be one of the files in the
                             resources/audio folder.
            repeat: Triggers repeat of the sound (use for theme song).
        """

        sound = pygame.mixer.Sound(audio_paths[audio_file_name])

        if repeat:
            sound.play(-1)
        else:
            sound.play()

        return
