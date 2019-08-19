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
    def __init__(self, surface):

        self.screen = surface
        self.pages = []
        self.current_page = None
        self.in_menus = True

        return

    def display(self):

        self.current_page.display(self.screen)

        return

    def is_in_menus(self):

        return self.in_menus

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

        return

    # Arg: menu_page Menu page to be added to the MenuManager
    def add_menu_page(self, menu_page):

        self.pages.append(menu_page)

        return

    def exit_menus(self):

        self.in_menus = False

    def enter_menus(self, to_page = None):

        self.in_menus = True

        if to_page != None:

            self.go_to(to_page)

    def update(self, user_events):

        self.current_page.update()

        mouse = pygame.mouse.get_pos()

        for event in user_events:

            if (event.type == pygame.MOUSEBUTTONUP):

                for button in self.current_page.buttons:

                    if (button.is_clicked(mouse[0], mouse[1])):

                        button.perform_click_action()

        return
