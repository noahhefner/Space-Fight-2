import pygame
import Constants

pygame.init()

class TextButton(pygame.sprite.Sprite):

    def __init__(self, text = "UNNAMED", to_page = "NONE"):

        super(TextButton, self).__init__()

        self.text = str(text)
        self.to_page = to_page
        self.color = Constants.BUTTONCOLOR
        self.font = Constants.BUTTONFONT
        self.image = self.font.render(self.text, False, self.color)
        self.rect = self.image.get_rect()

        return

    def get_to_page(self):

        return self.to_page

        return

    def __hover(self):

        (mouse_x, mouse_y) = pygame.mouse.get_pos()

        if mouse_x in range(self.rect.x, self.rect.x + self.rect.width) \
        and mouse_y in range(self.rect.y, self.rect.y + self.rect.height):

            self.color = Constants.BUTTONHOVER

        else:
            self.color = Constants.BUTTONCOLOR

        self.image = self.font.render(self.text, False, self.color)

        return

    def display(self, surface):

        surface.blit(self.image, [self.rect.x, self.rect.y])

        return

    def update(self):

        self.__hover()

        return
