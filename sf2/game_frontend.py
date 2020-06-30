"""
Noah Hefner
Space Fight 2.0
GameFrontend Class
Last Edit: 6/28/2020
"""

# Imports
from game_backend import GameBackend
import pygame
from settings import settings_game
from settings import settings_program
from constants import BLACK

# Initialize pygame
pygame.init()


class GameFrontend:
    """
    Handles frontend visuals for GameBackend object.

    Attributes:
        screen (pygame.display): Surface to blit the game objects to.
        clock (pygame.time.Clock): Used to set/cap game FPS.
        backend (GameBackend): The GameBackend object to be shown.
    """

    def __init__(self, screen, clock):
        """
        Instantiate a new GameFrontend object.
        """

        self.screen = screen
        self.clock = clock
        self.backend = GameBackend()

    def update(self):
        """
        Get user events, update backend w/ those events.

        Returns:
            playing (bool): True for continue game, False for end game.
        """

        self.__update_window_title()
        user_events = pygame.event.get()
        playing = self.backend.update(user_events)

        return playing

    def display(self):
        """
        Blit everything from backend to the screen.
        """

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

            x = (settings_game["hud_spacing"] * (i + 1)) + \
                (i * self.backend.hud.heart.rect.width)
            y = settings_game["hud_spacing"]

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

        # Flip the screen
        pygame.display.flip()

        # Tick clock
        self.clock.tick(settings_program["fps"])

    def __update_window_title (self):
        """
        Update the window title to include current fps count.
        """

        fps = str(int(self.clock.get_fps()))
        pygame.display.set_caption("SPACE FIGHT 2.0 - FPS: " + fps)
