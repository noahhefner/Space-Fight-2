# Noah Hefner
# Space Fight 2.0
# settings Class
# Last Edit: 1/2/2017

class Settings(object):
    """ Holds variables for the game settings. """

    def __init__ (self):
        """ Initializes settings class.  """

        self.player_type_string = "player_white.png"
        self.bullet_type_string = "bullet_red.png"
        self.bullet_speed = 15
        self.cursor_type = "cursor_red.png"
        self.screen_width = 1920
        self.screen_height = 1080
        self.active_screen = "MENU"
        self.coins = 0
        self.player_speed = 5
        self.player_start_lives = 3
        self.player_start_ammo = 100
