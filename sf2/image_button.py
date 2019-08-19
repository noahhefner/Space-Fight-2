"""
Noah Hefner
Space Fight 2.0
ImageButton Class
Last Edit: 8/16/2019
"""

import pygame
import os

pygame.init()

class ImageButton(pygame.sprite.Sprite):
    """
    Defines a button with a picture as its image.

    Attributes:
        image (pygame.image): Image path for the button picture.
        rect (pygame.image.rect): Position, height, width values for image.
        click_actions (list): Functions to run when the button is pressed.
        click_actions_args (list of lists): Lists of parameters that go with the click_actions.
    """

    def __init__(self, image_string, click_actions = None, click_actions_args = None):
        """
        Initialize an ImageButton object.

        Parameters:
            image_string (str): Image path to the picure for the button.
            click_actions (list): Functions to run when the button is pressed.
            click_actions_args (list of lists): Lists of parameters that go with the click_actions.
        """

        super(ImageButton, self).__init__()

        self.image = pygame.image.load(os.path.abspath("sf2/" + image_string)).convert()
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

    def display(self, surface):

        surface.blit(self.image, [self.rect.x, self.rect.y])

        return

    def is_clicked(self, x, y):

        return (x  in range(self.rect.x, (self.rect.x + self.rect.width)) and y in range(self.rect.y, (self.rect.y + self.rect.height)))

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