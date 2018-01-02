# Noah Hefner
# Space Fight 2.0
# Drop Class
# Last Edit: 12/17/2017

class Drop(pygame.sprite.Sprite):
    """ Powerups that drop when an alien is killed. """
    """ Restrict usage of this method to only recieve sprites with drops. """

    def __init__(self, alien):

        super(Alien, self)__init__()

        drop_image_list = ["drop_ammo.png", "drop_coin.png", "drop_life.png"]

        self.image = pygame.image.load(drop_image_list[alien.drop])
        self.rect = self.imge.get_rect()
        self.rect.x = (alien.rect.x + (alien.rect.width / 2)) - self.rect.width /  2
        self.rect.y = (alien.rect.y + (alien.rect.height / 2)) - self.rect.height / 2
        self.dropped_frames = 0

    def update(self):
        """ Times the drop for dropped_frames. """

        if self.dropped_frames == 360:

            self.kill()
