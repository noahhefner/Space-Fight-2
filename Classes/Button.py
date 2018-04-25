# Noah Hefner
# Space Fight 2.0
# Button Class
# Last Edit: 3/8/2018

import pygame
pygame.init()

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

class Button(pygame.sprite.Sprite):
    """ Buttons can be either images or text strings. """

    def __init__(self, image, scale = 1, highlight = False):
        """ Initializes button class.
        Args:
            image (string): image string or text to be made a button.
            scale (int): image scale
            highlight (boolean): should the text be highlighted when the cursor
                                 moves over it
        """

        super(Button, self).__init__()

        self.is_text = False

        if image.find(".png") == -1 and image.find(".jpeg") == -1 and image.find(".jpg") == -1:

            self.font = pygame.font.SysFont('04B', 80, False, False)
            self.default_color = WHITE
            self.color = WHITE
            self.text = str(image)
            self.image = self.font.render(self.text, False, self.color)
            self.highlight_color = RED
            self.is_text = True
            self.highlight = True

        else:

            self.image = pygame.image.load(image).convert()
            self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, [self.rect.width * scale, self.rect.height * scale])

        return

    def update(self):
        """ Highlight the text if the button is text and the cursor is on it. """

        if self.is_text:

            (mouse_x, mouse_y) = pygame.mouse.get_pos()

            if mouse_x in range(self.rect.x, self.rect.x + self.rect.width) \
            and mouse_y in range(self.rect.y, self.rect.y + self.rect.height) and self.highlight:

                self.color = self.highlight_color

            else:
                self.color = self.default_color

            self.image = self.font.render(self.text, False, self.color)

        else:

            return

    def position(self, position):
        """ Sets rect attributes to the given position.
        Args:
            position (tuple): tuple value of x and y positions for which the
            rect values will be assigned
        """

        self.rect.x = position[0]
        self.rect.y = position[1]

        return

    def is_clicked(self, mouse_pos):
        """ Returns boolean True if cursor is clicked within rect boundaries
        and False if outside rect boundaries.
        Args:
            mouse_pos (tuple): position of the cursor
        """

        if mouse_pos[0] in range(self.rect.x, self.rect.x + self.rect.width) and \
        mouse_pos[1] in range(self.rect.y, self.rect.y + self.rect.height):

           return True

        else:

           return False
