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

""" - - NEW METHOD FOR SETTINGS - - """

settings = {}
settings["player_type_string"] = "player_white.png"
settings["bullet_type_string"] = "bullet_red.png"
settings["cursor_type_string"] = "cursor_red.png"
settings["active_screen"] = "menu"
settings["player_start_ammo"] = 100
settings["player_start_lives"] = 3
settings["player_speed"] = 5
settings["bullet_speed"] = 15
settings["screen_width"] = 1920
settings["screen_height"] = 1080
settings["coins"] = 0
