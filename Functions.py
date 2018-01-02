# Noah Hefner
# Space Fight 2.0
# Functions
# Last Edit: 12/17/2017

def get_current_time():
    """ Returns current time. """

    return time.time()

def get_bullet_vel(speed):
    """ Returns vel_x and vel_y attributes for bullets. """

    [mouse_x, mouse_y] = pygame.cursor.get_pos()

    angle = math.atan2(game.player.rect.center[1]-mouse_y,
    game.player.rect.center[0]-mouse_x)

    x_vel = math.cos(angle) * (-1 * speed)
    y_vel = math.sin(angle)  * (-1 * speed)

    return [x_vel, y_vel]

def get_alien_multiplier(total_frames):
    """ Returns appropriate speed multiplier for aliens given time. """

    return round(total_frames / 3600)

def get_alien_vel():
    """ Set vel_x and vel_y attributes for alien. """

    x_diff = game.player.rect.x - self.rect.center[0]
    y_diff = game.player.rect.y - self.rect.center[1]

    angle = math.atan2(y_diff, x_diff)

    vel_y = math.sin(angle)
    vel_x = math.cos(angle)

    return [vel_x, vel_y]

def random_alien_spawn(screen_width, screen_height):
    """ Returns a random position off-screen for alien spawn. """

    position = []
    x = None
    y = None

    left_right = random.randrange(0,2)
    top_bottom = random.randrange(0,2)

    if left_right = 0:

        x = random.randrange(-100, -600)

    else:

        x = random.randrange(screen_width + 100, screen_width + 600)

    position.append(x)

    if top_bottom == 0:

        y = random.randrange(-100,-600)

    else:

        y = random.randrange(screen_height + 100, screen_height + 600)

    position.append(y)

    return position

def draw_sprite(sprite, surface):
    """ Draw image to the screen.
     Args:
         surface (surface): destination for text to be drawn.
    """

    surface.blit(self.image, [sprite.rect.x, sprite.rect.y])