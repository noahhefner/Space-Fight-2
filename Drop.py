# Noah Hefner
# Space Fight 2.0
# Drop Class
# Last Edit: 12/17/2017

class Drop(pyame.sprite.Sprite):
    """ Powerups that drop when an alien is killed. """
    """ Restrict usage of this method to only recieve sprites with drops. """

    def __init__(self, alien):

        super(Alien, self)__init__()

        if alien.drop == 0:

            self.image_string = "ammo image"

        elif alien.drop == 1:

            self.image_string = "life drop"

        elif alien.drop == 2:

            self.image_string = game.player.special

        elif alien.drop == 3:

            self.image_string = "coin drop"

        else return False

        self.image = pygame.image.load(self.image_string)
        self.rect = self.imge.get_rect()
        self.rect.x = (alien.rect.x + (alien.rect.width / 2)) - self.rect.width /  2
        self.rect.y = (alien.rect.y + (alien.rect.height / 2)) - self.rect.height / 2
        self.dropped_frames = 0

    def update(self):

        TODO: "lower opacity of sprite over time"

        if self.dropped_frames == 360:

            self.kill()
