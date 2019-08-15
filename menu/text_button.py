"""
Noah Hefner
Space Fight 2.0
Text Button Class
Last Edit: 8/15/2019
"""

import pygame

pygame.init()

class TextButton(pygame.sprite.Sprite):

    def __init__(self, font, text = "NOTEXT", click_action = None, color = [255, 255, 255]):

        super(TextButton, self).__init__()

        self.image = font.render(text, False, color)
        self.rect = self.image.get_rect()
        self.click_action = click_action

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

        if (self.click_action != None):
            self.click_action()
        else:
            pass

        return

    def is_clicked(self, x, y):

        clicked = (x  in range(self.rect.x, (self.rect.x + self.rect.width)) and y in range(self.rect.y, (self.rect.y + self.rect.height)))
        return clicked

    def display(self, surface):

        surface.blit(self.image, [self.rect.x, self.rect.y])

        return
