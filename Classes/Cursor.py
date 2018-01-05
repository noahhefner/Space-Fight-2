# Noah Hefner
# Space Fight 2.0
# Menu Class
# Last Edit: 1/5/2018

class Cursor(pygame.sprite.Sprite):
  """ Cursor that is blitted in place of the windows cursor.

  Args:
    image_string (str): Image of the cursor.

  Attributes:
    image (pygame sprite): Pygame sprite image that uses the
    image_string arg.
    rect (pygame sprite rect): Rect attributes for sprite image.

  """

  def __init__ (self):

    super(Cursor, self).__init__()

    self.image = pygame.image.load("cursor_red.png").convert()
    self.image.set_colorkey(BLACK)

    self.rect = self.image.get_rect()

  def update(self):
    """ Get the mouse position. Set the center of the cursor to that
    point.

    """

    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    self.rect.center = (mouse_x,mouse_y)

  def draw(self, screen):
    """ Blit the cursor to the screen.

    """

    screen.blit(self.image, [self.rect.x, self.rect.y])
