# Noah Hefner
# Space Fight 2.0
# Button Class
# Last Edit: 12/17/2017

class Button(pygame.sprite.Sprite):
    """ Buttons can be either images or text strings. """

    def __init__(self, image):
        """ Initializes button class.
        Args:
            image (string): image string or text to be made a button.
        """

        super(Button, self).__init__()

        self.is_text = False

        if image.find(".png") == -1 and image.find(".jpeg") == -1 and image.find(".jpg") == -1:

            self.font = pygame.font.SysFont('ARCADECLASSIC', 25, False, False)
            self.default_color = WHITE
            self.color = WHITE
            self.text = str(image)
            self.image = self.font.render(self.text, False, self.color)
            self.rect = self.image.get_rect()
            self.highlight_color = RED
            self.is_text = True

        else:

            self.image = pygame.image.load(image).convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()

    def update(self):
        """ Highlight the text if the button is text and the cursor is on it. """

        if self.is_text:

            (mouse_x, mouse_y) = pygame.mouse.get_pos()

            if mouse_x in range(self.rect.x, self.rect.x + self.rect.width):

                self.color = self.highlight_color

            else:

                self.color = self.default_color

            self.image = self.font.render(self.text, False, self.color)