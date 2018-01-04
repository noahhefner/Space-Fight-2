# Noah Hefner
# Space Fight 2.0
# Scene Class
# Last Edit: 1/2/2017

class Scene(object):
    """  """

    def __init__ (self, sprite_array):

        self.sprite_array = sprite_array

        for sprite in sprite_array:

            sprite[0].rect.x = sprite[1]
            sprite[0].rect.y = sprite[2]

    def update(self):

        for sprite in self.sprite_array:

            sprite[0].update()

    def draw(self, surface):

        for sprite in self.sprite_array:

            sprite[0].draw(surface)
