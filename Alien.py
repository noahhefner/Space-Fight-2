# Noah Hefner
# Space Fight 2.0
# Alien Class
# Last Edit: 12/17/2017

class Alien(pygame.sprite.Sprite):
    """ In game alien entity. """

    def __init__(self):
        """ Initiate alien class. """

        super(Alien, self).__init__()

        self.image = pygame.image.load("alien_level_one.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos_initial = Functions.random_alien_spawn()
        self.rect.x, self.rect.y = self.pos_initial[0], self.pos_initial[1]
        self.speed = 20
        self.speed_multiplier = 1
        self.drop = random.randrange(0,10)

    def update(self):
        """ Moves the alien. """

        vel = Functions.get_alien_vel()
        multiplier = Functions.get_alien_multiplier()

        self.rect.x += vel[0] * multiplier
        self.rect.y += vel[1] * multiplier
