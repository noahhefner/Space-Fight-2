import pygame
pygame.init()

class Button:

    def __init__ (self, image, action):

        super(Button, self).__init__()

        self.image = pygame.image.load(image)
        self.action = action
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def execute_action (self):

        self.action()
