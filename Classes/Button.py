# Noah Hefner
# Space Fight 2.0
# Button Class
# Last Edit: 1/5//2018

class Button(pygame.sprite.Sprite):
    """ Buttons can be either images or text strings. """

    def __init__(self, image, x2_image_scale = False, highlight = False):
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
            self.highlight = True

        else:

            self.image = pygame.image.load(image).convert()
            self.image.set_colorkey(BLACK)

            if x2_image_scale:

                self.image = pygame.transform.scale2x(self.image)

            self.rect = self.image.get_rect()

        return

    def update(self):
        """ Highlight the text if the button is text and the cursor is on it. """

        if self.is_text:

            (mouse_x, mouse_y) = pygame.mouse.get_pos()

            if mouse_x in range(self.rect.x, self.rect.x + self.rect.width) \
            and self.highlight:

                self.color = self.highlight_color

            else:

                self.color = self.default_color

            self.image = self.font.render(self.text, False, self.color)

        else:

            return

    def position(self, position):

        self.rect.x = position[0] - ((1/2) * self.rect.x)
        self.rect.y = position[1] - ((1/2) * self.rect.y)

        return
