

class TextButton(pygame.sprite.Sprite):

    def __init__(self, text = "UNNAMED", to_page = "NONE"):

        super(Button, self).__init__()

        self.text = text
        self.to_page = to_page
        self.color = Constants.BUTTONCOLOR
        self.image = self.font.render(self.text, False, self.color)
        self.image = pygame.transform.scale(self.image, \
        [self.rect.width * Constants.BUTTONTEXTSCALE, \
        self.rect.height * Constants.BUTTONTEXTSCALE])
        self.image = self.image.get_rect()

        return

    def get_to_page(self):

        return self.to_page

    def __hover(self):

        (mouse_x, mouse_y) = pygame.mouse.get_pos()

        if mouse_x in range(self.rect.x, self.rect.x + self.rect.width) \
        and mouse_y in range(self.rect.y, self.rect.y + self.rect.height):

            self.color = Constants.BUTTONHOVER

        else:
            self.color = Constants.BUTTONCOLOR

        self.image = self.font.render(self.text, False, self.color)

    def display(self, surface):

        surface.blit(self.image, [self.rect.x, self.rect.y])

    def update(self):

        self.__hover()
