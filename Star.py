# Noah Hefner
# Space Fight 2.0
# Star Class
# Last Edit: 12/17/2017

class Star(pygame.sprite.Sprite):
    """ Star sprite images used for background. """

    def __init__ (self, image_string):

        super(Star, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.velx = random.randrange(1,4)
        self.vely = random.ranrange(-3,0)

    def update(self):
        """ Add the velx and vely attributes to the rect.x and rect.y
        positions, respectively. If the star goes off the top of the screen,
        reset the posiiton to the bottom of the screen.

        """

        self.rect.x += self.velx
        self.rect.y += self.vely

        if self.rect.y + self.rect.height < 0:

            self.rect.y = SCREEN_HEIGHT
