# Noah Hefner
# Menu Manager for Pygame
# Last Edit: 2.15.2019

from MenuPage import MenuPage
import pygame

class MenuManager():

    # Must have home_screen created first before creating menu
    def __init__(self, home_screen):

        self.page_list = [home_screen]
        self.current_page = home_screen

        return

    def display(self, surface):

        self.current_page.display(surface)

        return

    # Arg: page_name The string name of the next page
    # Precondition: page_name is in the menumanager
    def set_current_page(self, page_name):

        success = False

        for page in self.page_list:

            if page.name == page_name:

                self.current_page = page
                success = True

        if not success:

            print("ERROR: " , page_name, "NOT IN MENU MANAGER")

    # Arg: menu_page Menu page to be added to the MenuManager
    def add_menu_page(self, menu_page):

        if isinstance(menu_page, MenuPage):

            self.page_list.append(menu_page)

        else:

            print("ERROR: " , menu_page, " IS NOT A MENUPAGE")

        return

    def is_clicked(self, button, mouse_pos):

        clicked = False

        mouse_x, mouse_y = mouse_pos[0], mouse_pos[1]

        if mouse_x in \
        range(button.rect.x, button.rect.x + button.rect.width) and \
        mouse_y in \
        range(button.rect.y, button.rect.y + button.rect.height):

            clicked = True

        return clicked

    def update(self, event):

        self.current_page.set_coords()
        self.current_page.update()

        mouse = pygame.mouse.get_pos()

        new_page = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            for button in self.current_page.text_buttons:

                if self.is_clicked(button, mouse) and \
                button.get_to_page() != None:

                    if button.get_to_page() == "QUIT" or \
                    button.get_to_page() == "GAME":

                        return button.get_to_page()

                    else:

                        next_page = button.get_to_page()
                        new_page = True

            for button in self.current_page.image_buttons:

                if is_clicked(button, mouse) and \
                button.get_to_page() != None:

                    next_page = button.get_to_page()
                    new_page = True

        if new_page:

            self.set_current_page(next_page)

        new_page = False
