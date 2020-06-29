"""
Noah Hefner
Space Fight 2.0
Page Class
Last Edit: 6/29/2020
"""

# Imports
import pygame
from button import Button
from constants import BLACK
from settings import settings

# Initialize pygame
pygame.init()


class MenuManager:
    """
    Menu manager for pygame.

    Attributes:
        pages (List): List of pages in the menu manager.
        current_page (Page): Page currently being displayed.
        screen (pygame.display): Surface to blit the pages and game to.
        clock (pygame.time.Clock): Used to set/cap game FPS.
        start_page_set (Boolean): Switch that checks if start page has been set.
    """

    def __init__ (self, screen, clock):
        """
        Instantiate a MenuManager object.
        """

        self.pages = []
        self.current_page = None
        self.screen = screen
        self.clock = clock
        self.start_page_set = False
        self.exiting = False

    def add_page (self, new_page):
        """
        Adds a page to the menu manager.

        Arguments:
            new_page (Page): Page to be added to the menu manager.
        """

        self.pages.append(new_page)

    def navigate (self, page_id):
        """
        Sets the currently showing page using the id attribute of Page class.

        Arguments:
            page_id (String/Int): ID of the desired page destination.

        NOTE: See Page class for more info on page id's.
        """

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
        """
        Handles user events. Also checks if a start page has been set. This
        function will prevent the program from running if a sart page has not
        beem set.

        Returns:
            Boolean: True if program execution should continue, False otherwise.
        """

        if not self.start_page_set:

            print("Start page not set!")
            exit()

        if self.exiting:

            self.exiting = False

            return False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                for element in self.current_page.elements:

                    if isinstance(element, Button):

                        if element.is_clicked(mouse_pos):

                            element.execute_action()

        return True

    def exit_menu (self):

        self.exiting = True

    def kill_program (self):

        exit()

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
