
from game_backend import GameBackend
import pygame
from settings import settings
from constants import BLACK

pygame.init()


class GameFrontend:

    def __init__(self):

        self.screen = pygame.display.set_mode(
            [settings["screen_width"], settings["screen_height"]])
        self.clock = pygame.time.Clock()
        self.backend = GameBackend()

    def update(self):

        user_events = pygame.event.get()
        playing = self.backend.update(user_events)

        return playing

    def display(self):

        self.screen.fill(BLACK)

        for star in self.backend.get_stars():

            self.screen.blit(star.image, [star.get_x(), star.get_y()])

        for bullet in self.backend.get_bullets():

            self.screen.blit(bullet.image, [bullet.get_x(), bullet.get_y()])

        for explosion in self.backend.get_explosions():

            self.screen.blit(explosion.image, [explosion.get_x(),
                                               explosion.get_y()])

        for drop in self.backend.get_drops():

            self.screen.blit(drop.image, [drop.get_x(), drop.get_y()])

        for alien in self.backend.get_aliens():

            self.screen.blit(alien.image, [alien.get_x(), alien.get_y()])

        self.screen.blit(self.backend.player.image,
                         [self.backend.player.get_x(),
                          self.backend.player.get_y()])

        pygame.display.flip()

        self.clock.tick(settings["fps"])

        return
