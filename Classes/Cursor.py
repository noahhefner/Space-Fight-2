# Noah Hefner
# Space Fight 2.0
# Menu Class
# Last Edit: 1/5/2018

import math
import pygame
import time

# Constants
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
GREY = [105, 105, 105]
RED = [255, 0, 0]

pygame.init()

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

    self.image = pygame.image.load("/home/noahhefner/Git/Space-Fight-2/Images/cursor_red.png")
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
