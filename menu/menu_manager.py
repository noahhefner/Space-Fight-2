"""
Noah Hefner
Space Fight 2.0
Menu Manager Class
Last Edit: 8/15/2019
"""

import pygame

pygame.init()


class MenuManager():

    # Must have home_screen created first before creating menu
    def __init__(self):

        self.pages = []
        self.current_page = None

        return

    def display(self, surface):

        self.current_page.display(surface)

        return

    # Arg: page_name The string name of the next page
    # Precondition: page_name is in the menumanager
    def go_to(self, page_name):

        success = False

        for page in self.pages:

            if page.page_name == page_name:

                self.current_page = page
                success = True

        if not success:

            print("ERROR: " , page_name, "NOT IN MENU MANAGER")


    # Arg: menu_page Menu page to be added to the MenuManager
    def add_menu_page(self, menu_page):

        self.pages.append(menu_page)

        return

    def update(self, event):

        self.current_page.update()

        mouse = pygame.mouse.get_pos()

        if (event.type == pygame.MOUSEBUTTONUP):

            for button in self.current_page.buttons:

                if (button.is_clicked(mouse[0], mouse[1])):

                    button.perform_click_action()

        return
