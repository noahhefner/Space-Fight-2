import pygame

class ImageButton(pygame.sprite.Sprite):

    def __init__(self, image_string, to_page = "NONE", hover_image_string = "NONE"):

        super(ImageButton, self).__init__()

        self.image = pygame.image.load(image_string)
        self.base_image = pygame.image.load(image_string)

        if hover_image_string != "NONE":
            self.hover_image = pygame.image.load(hover_image_string)
        else:
            self.hover_image_string = hover_image_string

        self.to_page = to_page
        self.rect = self.image.get_rect()

        return

    def get_to_page(self):

        return self.to_page

    def set_position(self, x, y):

        self.rect.x = x
        self.rect.y = y

        return

    def __hover(self):

        if self.hover_image_string == "NONE":

            pass

        else:

            (mouse_x, mouse_y) = pygame.mouse.get_pos()

            if mouse_x in range(self.rect.x, self.rect.x + self.rect.width) \
            and mouse_y in range(self.rect.y, self.rect.y + self.rect.height):

                self.image = self.hover_image

            else:

                self.image = self.base_image

        return

    def display(self, surface):

        surface.blit(self.image, [self.rect.x, self.rect.y])

        return

    def update(self):

        self.__hover()

        return
