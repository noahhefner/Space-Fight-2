"""
Noah Hefner
Space Fight 2.0
Button Class
Last Edit: 6/29/2020
"""

# Imports
import pygame
from constants import BLACK

# Initialize pygame
pygame.init()


class Button(pygame.sprite.Sprite):
    """
    Button object for menu manager.

    Attributes:
        image (pygame.image): Image for button.
        action (function): Function to execute when button is pressed.
        rect (pygame.image.rect): Position, height, width values for image.
    """

    def __init__ (self, image, action, *action_args, pos = [0,0]):
        """
        Instantiate a button object.

        Arguments:
            image (string): Path of image file to be used for button.
            action (function): Function to execute when button is pressed.
            pos (tuple): XY position for the button.
        """

        super(Button, self).__init__()

        self.image = pygame.image.load(image)
        self.action = action
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.action_args = action_args

    def is_clicked (self, mouse_pos):
        """
        Returns true if the mouse cursor position is on this sprite.

        Arguments:
            mouse_pos (tuple): XY position of the cursor.
        """

        # Check x axis
        within_x = mouse_pos[0] >= self.rect.x and mouse_pos[0] <= self.rect.x + self.rect.width

        # Check y axis
        within_y = mouse_pos[1] >= self.rect.y and mouse_pos[1] <= self.rect.y + self.rect.height

        # True if within x and y area
        return within_x and within_y

    def set_pos (self, pos):
        """
        Set position of the button.

        Arguments:
            pos (tuple): XY position to set the button to.
        """

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def execute_action (self):
        """
        Execute function linked to this button.
        """

        if (self.action != None):

            self.action(*self.action_args)
