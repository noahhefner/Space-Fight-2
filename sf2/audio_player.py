"""
Noah Hefner
Space Fight 2.0
AudioPlayer Class
Last Edit: 6/30/2020
"""

# Imports
import pygame
from strings import audio_paths

# Initialize pygame
pygame.init()


class AudioPlayer:
    """
    Plays sounds.
    """

    def __init__(self):
        """
        Instantiate a new AudioPlayer object.
        """

    def stop (self):
        """
        End all audio from the mixer.
        """

        pygame.mixer.stop()

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
