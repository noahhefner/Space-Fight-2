
import pygame
from strings import strings

pygame.init()

class AudioPlayer:

    def __init__():

        self.bullet_fire = pygame.mixer.Sound(strings["bullet_fire"])
        self.explosion = pygame.mixer.Sound(strings["explosion"])
        self.pickup_bullets = pygame.mixer.Sound(strings["pickup_bullets"])
        self.pickup_coin = pyugame.mixer.Sound(strings["pickup_coin"])
        self.pickup_life = pygame.mixer.Sound(strings["pickup_life"])
        self.theme = pygame.mixer.Sound(strings["theme"])

    def play_bullet_fire(self):

        self.bullet_fire.play()

    def play_explosion(self):

        self.explosion.play()

    def play_pickup_bullets(self):

        self.pickup_bullets.play()

    def play_pickup_coin(self):

        self.pickup_coin.play()

    def play_pickup_life(self):

        self.pickup_life.play()

    def play_theme(self):

        self.theme.play(-1)
