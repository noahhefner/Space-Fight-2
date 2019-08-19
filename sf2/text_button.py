"""
Noah Hefner
Space Fight 2.0
Text Button Class
Last Edit: 8/15/2019
"""

import pygame

pygame.init()

class TextButton(pygame.sprite.Sprite):

    def __init__(self, font, text = "NOTEXT", click_actions = [], click_actions_args = [[]], color = [255, 255, 255]):

        super(TextButton, self).__init__()

        self.image = font.render(text, False, color)
        self.rect = self.image.get_rect()
        self.click_actions = click_actions
        self.click_actions_args = click_actions_args

        return

    def update(self):

        return

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

        return True

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

        return True

    def perform_click_action(self):

        for i in range(len(self.click_actions)):

            action = self.click_actions[i]
            args = self.click_actions_args[i]

            if (action != None and args != None):
                action(*args)
            elif (self.click_actions[i] != None and self.click_actions_args[i] == None):
                action()
            else:
                pass

        return True

    def is_clicked(self, x, y):

        clicked = (x  in range(self.rect.x, (self.rect.x + self.rect.width)) and y in range(self.rect.y, (self.rect.y + self.rect.height)))
        return clicked

    def display(self, surface):

        surface.blit(self.image, [self.rect.x, self.rect.y])

        return
