# Noah Hefner
# Space Fight 2.0
# AudioPlayer Class
# Last Edit: 8/2/2019

import pygame
from strings import audio_paths

pygame.init()


class AudioPlayer:

    def __init__(self):

        self.bullet_fire = pygame.mixer.Sound(audio_paths["bullet_fire"])
        self.explosion = pygame.mixer.Sound(audio_paths["explosion"])
        self.hitmarker = pygame.mixer.Sound(audio_paths["hitmarker"])
        self.pickup_bullets = pygame.mixer.Sound(audio_paths["pickup_bullets"])
        self.pickup_coin = pygame.mixer.Sound(audio_paths["pickup_coin"])
        self.pickup_life = pygame.mixer.Sound(audio_paths["pickup_life"])
        self.theme = pygame.mixer.Sound(audio_paths["theme"])

    def play_bullet_fire(self):

        self.bullet_fire.play()

    def play_explosion(self):

        self.explosion.play()

    def play_hitmarker(self):

        self.hitmarker.play()

    def play_pickup_bullets(self):

        self.pickup_bullets.play()

    def play_pickup_coin(self):

        self.pickup_coin.play()

    def play_pickup_life(self):

        self.pickup_life.play()

    def play_theme(self):

        self.theme.play(-1)
