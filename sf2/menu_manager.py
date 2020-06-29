
import pygame
from constants import BLACK
from settings import settings
pygame.init()

class MenuManager:

    def __init__ (self):

        self.pages = []
        self.current_page = None

        self.screen = pygame.display.set_mode(
            [settings["screen_width"], settings["screen_height"]])
        pygame.display.set_caption("SPACE FIGHT 2.0")
        self.clock = pygame.time.Clock()

        self.start_page_set = False

    def add_page (self, new_page):

        self.pages.append(new_page)

    def navigate (self, page_id):

        for page in self.pages:

            if page.id == page_id:

                self.current_page = page

                return

    def set_start_page (self, start_page):
        """
        Set a start page for the menu manager. This function requires that the
        start page already be in the menu manager.
        """

        for page in self.pages:

            if (page.id == start_page.id):

                self.current_page = start_page
                self.start_page_set = True

    def update (self):

        if not self.start_page_set:

            print("Start page not set!")
            return False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                for element in self.current_page.elements:

                    if element.is_clicked(mouse_pos):

                        element.execute_action()

        return True

    def display (self):
        """
        Blit everything from backend to the screen.
        """

        # Fill background
        self.screen.fill(BLACK)

        # Display current screen
        self.current_page.display(self.screen)

        pygame.display.flip()

        self.clock.tick(settings["fps"])
