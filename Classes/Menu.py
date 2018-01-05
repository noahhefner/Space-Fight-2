# Noah Hefner
# Space Fight 2.0
# Menu Class
# Last Edit: 1/5/2018

class Menu(object):
    """ Holds code regarding menu screen elements. """

    def __init__(self):
        """ Initiates menu class. """

        # Cursor sprite
        self.cursor = Cursor()
        # TODO: Add cursor upgrades

        # Sprite groups that hol1d items for each screen
        self.menu_screen_home = pygame.sprite.Group()
        self.menu_screen_upgrades = pygame.sprite.Group()
        self.menu_screen_active = self.menu_screen_home()

        # Arrays to hold positions for items for each screen
        self.array_menu_home = Array(Settings.screen_width, \
                                     Settings.screen_height, 5, 1)
        self.array_menu_upgrades = Array(Settings.screen_width, \
                                         Settings.screen_height, 5, 4)

        """" - - - Home Menu Items - - - """
        # Buttons
        self.button_start = Button("START")
        self.button_upgrades = Button("UPGRADES")
        self.button_quit = Button("QUIT")

        # Add home menu items to home menu group
        self.menu_screen_home.add(self.button_start)
        self.menu_screen_home.add(self.button_upgrades)
        self.menu_screen_home.add(self.button_quit)

        # Grid home menu buttons
        self.button_start.position(self.array_menu_home.position(1,1))
        self.button_upgrades.position(self.array_menu_home.position(1,2))
        self.button_quit.position(self.array_menu_home.position(1,3))

        """ - - - Upgrade Menu Items - - - """
        """ Buttons """
        self.player_blue_button = Button("player_blue.png", True)
        self.player_green_button = Button("player_green.png", True)
        self.player_white_button = Button("player_white.png", True)
        self.player_yellow_button = Button("player_yellow.png", True)
        # TODO: Add purple player

        self.bulelt_blue_button = Button("bullet_blue.png", True)
        self.bullet_green_button = Button("bullet_green.png", True)
        self.bullet_purple_button = Button("bullet_purple.png", True)
        self.bullet_red_button = Button("bullet_red.png", True)
        self.bullet_yellow_button = Button("bullet_yellow.png", True)

        self.boost_speed_button = Button("SPEED (10 COINS)")
        self.boost_lives_button = Button("LIVES (30 COINS)")
        self.boost_ammo_button = Button("AMMOS (20 COINS)")

        self.current_button = Button("CURRENT", False, False)

        # Add upgrade menu items to upgrade menu group
        self.menu_screen_upgrades.add(self.player_blue_button)
        self.menu_screen_upgrades.add(self.player_green_button)
        self.menu_screen_upgrades.add(self.player_white_button)
        self.menu_screen_upgrades.add(self.player_yellow_button)

        self.menu_screen_upgrades.add(self.bulelt_blue_button)
        self.menu_screen_upgrades.add(self.bullet_green_button)
        self.menu_screen_upgrades.add(self.bullet_purple_button)
        self.menu_screen_upgrades.add(self.bullet_red_button)
        self.menu_screen_upgrades.add(self.bullet_yellow_button)

        self.menu_screen_upgrades.add(self.boost_speed_button)
        self.menu_screen_upgrades.add(self.boost_lives_button)
        self.menu_screen_upgrades.add(self.boost_ammo_button)

        self.menu_screen_upgrades.add(self.current_button)

        # Grid upgrade menu buttons
        self.player_white_button.position(self.array_menu_upgrades.position(1,1))
        self.player_blue_button.position(self.array_menu_upgrades.position(1,2))
        self.player_green_button.position(self.array_menu_upgrades.position(1,3))
        self.player_yellow_button.position(self.array_menu_upgrades.position(1,4))

        self.bulelt_blue_button.position(self.array_menu_upgrades.position(2,2))
        self.bullet_green_button.position(self.array_menu_upgrades.position(2,3))
        self.bullet_purple_button.position(self.array_menu_upgrades.position(2,5))
        self.bullet_red_button.position(self.array_menu_upgrades.position(2,1))
        self.bullet_yellow_button.position(self.array_menu_upgrades.position(2,4))

        self.boost_speed_button.position(self.array_menu_upgrades.position(3,1))
        self.boost_lives_button.position(self.array_menu_upgrades.position(3,3))
        self.boost_ammo_button.position(self.array_menu_upgrades.position(3,5))

        return

    def process_user_events(self):
        """ Handle user input. """

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if self.menu_screen_active == self.menu_screen_home:

                    if pygame.sprite.collide_rect(self.cursor, \
                                                  self.button_start) or \
                    pygame.sprite.collide_rect(self.cursor, self.button_quit):

                        return True

                    else if pygame.sprite.collide_rect(self.cursor, \
                                                       self.button_upgrades):
                        self.menu_screen_active = self.menu_screen_upgrades

                if self.menu_screen_active == self.menu_scren

        return False

    @staticmethod
    def get_cursor_click(self, sprite):
        """"""

        [mouse_x, mouse_y] = pygame.mouse.get_pos()

        if mouse_x in range(sprite.rect.x, sprite.rect.x + sprite.rect.width) and \
           mouse_y in range(sprite.rect.y, sprite.rect.y + sprite.rect.height):

            to_screen = self.get_screen(sprite)

            return to_screen

        else:

            return False

    @staticmethod
    def get_screen(self, button):
        """ Returns the next screens sprite list from the given button tag. """

        if button.text == "START":

            return True

        if button.text == "QUIT":

            return True

        if button.text == "UPGRADES":

            return self.menu_screen_upgrades

        elif button.text == "SHIP":

            return self.menu_screen_upgrades_ship_type

        elif button.text == "BULLET":

            return self.menu_screen_upgrades_bullet_type

        elif button.text == "LIVES":

            return self.menu_screen_upgrades_start_lives

        else:

            return

    def update(self):
        """ Update the Text menu items. """

        self.menu_screen_active.update()

        return

    def display_frame(self, surface):
        """ Draw the sprites needed for the current screen. """

        self.menu_screen_active.draw()

        return

    def set_menu_resolution_margins(self):
        """ Adjust menu items for the current screen size. """

        count = 0

        for item in self.menu_screen_active:

            center_space_y = Settings.screen_height / (len(self.menu_screen_active) + 1)
            item.rect.y = (center_space_y * (1 + count)) - (item.rect.height / 2)
            item.rect.x = (Settings.screen_width / 2) - (item.rect.width / 2)

            count += 1

        return
