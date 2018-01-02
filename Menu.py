# Noah Hefner
# Space Fight 2.0
# Menu Class
# Last Edit: 12/17/2017

class Menu(object):
    """ Holds code regarding menu screen elements. """

    def __init__(self):
        """ Initiates menu class. """

        # Sprite Lists that hold items for each screen
        self.menu_screen_active = self.menu_items_home
        self.game_settings = ["player_white.png", "bullet_red.png"]

        self.menu_items_home = pygame.sprite.LayeredUpdates([pygame.sprite.Group])
        self.menu_items_upgrades = pygame.sprite.LayeredUpdates([pygame.sprite.Group])
        self.menu_items_upgrades_ship_type = pygame.sprite.LayeredUpdates([pygame.sprite.Group])
        self.menu_items_upgrades_bullet_type = pygame.sprite.LayeredUpdates([pygame.sprite.Group])
        self.menu_items_upgrades_start_lives = pygame.sprite.LayeredUpdates([pygame.sprite.Group])
        self.menu_items_upgrades_special = pygame.sprite.LayeredUpdates([pygame.sprite.Group])

        # Home menu page items
        self.button_start = Button("START")
        self.button_upgrades = Button("UPGRADES")
        self.button_quit = Button("QUIT")
        self.menu_items_home.add(self.button_start)
        self.menu_items_home.add(self.button_upgrades)
        self.menu_items_home.add(self.button_quit)

        # Upgrades menu page items
        self.button_ship_type = Button("SHIP")
        self.button_bullet_type = Button("BULLET")
        self.button_start_lives = Button("LIVES")
        self.menu_items_upgrades.add(self.button_ship_type)
        self.menu_items_upgrades.add(self.button_bullet_type)
        self.menu_items_upgrades.add(self.button_start_lives)

        # Ship type upgrade menu
        """ Picture Sprites """

    def process_user_events(self):
        """ Handle user input. """

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                for sprite in self.menu_screen_active:

                    next_screen = self.get_cursor_click(sprite)

                    if next_screen == 'game' or next_screen == 'quit':

                        return True

                    else:

                        self.menu_screen_active = next_screen

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

            return game

        if button.text == "QUIT":

            return done

        if button.text == "UPGRADES":

            return self.menu_items_upgrades

        elif button.text == "SHIP":

            return self.menu_items_upgrades_ship_type

        elif button.text == "BULLET":

            return self.menu_items_upgrades_bullet_type

        elif button.text == "LIVES":

            return self.menu_items_upgrades_start_lives

        else:

            return

    def update(self):
        """ Update the Text menu items. """

        for item in self.menu_screen_active:

            item.update()

    def display_frame(self, surface):
        """ Draw the sprites needed for the current screen. """

        for item in self.menu_screen_active:

            item.draw(surface)

    def set_menu_resolution_margins(self):
        """ Adjust menu items for the current screen size. """

        count = 0

        for item in self.menu_screen_active:

            center_space_y = SCREEN_HEIGHT / (len(self.menu_screen_active) + 1)
            item.rect.y = (center_space_y * (1 + count)) - (item.rect.height / 2)
            item.rect.x = (SCREEN_WIDTH / 2) - (item.rect.width / 2)

            count += 1
