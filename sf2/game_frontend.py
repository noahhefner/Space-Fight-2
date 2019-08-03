# Noah Hefner
# Space Fight 2.0
# Drop Class
# Last Edit: 7/28/2019

from game_backend import GameBackend
import pygame
from settings import settings
from constants import BLACK

pygame.init()


class GameFrontend:

    def __init__(self):

        self.screen = pygame.display.set_mode(
            [settings["screen_width"], settings["screen_height"]],
            pygame.FULLSCREEN)
        pygame.display.set_caption("SPACE FIGHT 2.0")
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.backend = GameBackend()

    def update(self):

        user_events = pygame.event.get()
        playing = self.backend.update(user_events)

        return playing

    def display(self):

        # Fill background
        self.screen.fill(BLACK)

        # Blit stars
        self.backend.get_stars().draw(self.screen)

        # Blit HUD
        self.screen.blit(self.backend.hud.counter_bullets.image,
                         [self.backend.hud.counter_bullets.rect.x,
                          self.backend.hud.counter_bullets.rect.y])

        self.screen.blit(self.backend.hud.counter_coins.image,
                         [self.backend.hud.counter_coins.rect.x,
                          self.backend.hud.counter_coins.rect.y])

        self.screen.blit(self.backend.hud.counter_score.image,
                         [self.backend.hud.counter_score.rect.x,
                          self.backend.hud.counter_score.rect.y])

        for i in range(self.backend.player.lives):

            x = (settings["hud_spacing"] * (i + 1)) + \
                (i * self.backend.hud.heart.rect.width)
            y = settings["hud_spacing"]

            self.screen.blit(self.backend.hud.heart.image, [x, y])

        # Blit bullets
        self.backend.get_bullets().draw(self.screen)

        # Blit explosions
        self.backend.get_explosions().draw(self.screen)

        # Blit drops
        self.backend.get_drops().draw(self.screen)

        # Blit aliens
        self.backend.get_aliens().draw(self.screen)

        # Blit player
        self.screen.blit(self.backend.player.image,
                         [self.backend.player.get_x(),
                          self.backend.player.get_y()])

        # Blit cursor
        self.screen.blit(self.backend.cursor.image,
                         [self.backend.cursor.get_x(),
                          self.backend.cursor.get_y()])

        pygame.display.flip()

        self.clock.tick(settings["fps"])

        return
