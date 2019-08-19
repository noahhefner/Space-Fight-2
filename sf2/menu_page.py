"""
Noah Hefner
Space Fight 2.0
MenuPage Class
Last Edit: 8/16/2019
"""

from settings import settings

class MenuPage():

    def __init__(self, page_name = "UNNAMED"):

        self.page_name = page_name
        self.buttons = []
        self.x_spacing = 10
        self.y_spacing = 10
        self.x_positioning = "left"
        self.y_positioning = "top"

    def set_x_positioning(self, x_positioning):

        if (x_positioning == "left" or x_positioning == "mid" or x_positioning == "right"):

            self.x_positioning = x_positioning
            self.set_coords()
            return True

        else:

            print("Invalid x axis positioning!")
            return False

    def set_y_positioning(self, y_positioning):

        if (y_positioning == "top" or y_positioning == "mid" or y_positioning == "bot"):

            self.y_positioning = y_positioning
            self.set_coords()
            return True

        else:

            print("Invalid x axis positioning!")
            return False

    def add_button(self, button):

        self.buttons.append(button)
        self.set_coords()

    def set_coords(self):

        # Set x coordinates for all the buttons
        for button in self.buttons:

            if self.x_positioning == "left":

                button.rect.x = self.x_spacing

            elif self.x_positioning == "mid":

                button.rect.x = (int(settings["screen_width"]) / 2) - \
                (button.rect.width / 2)

            elif self.x_positioning == "right":

                button.rect.x = int(settings["screen_width"]) - \
                self.x_spacing - button.rect.width

            else:

                print("Invalid x axis positioning")

        # Set y coordinates for all the buttons
        count = 0
        for button in self.buttons:

            if self.y_positioning == "top":

                button.rect.y = ((count + 1) * self.y_spacing) + \
                (count * self.buttons[0].rect.height)

            elif self.y_positioning == "mid":

                # Calculations for mid positioning
                total_height = self.buttons[0].rect.height * \
                len(self.buttons) + \
                self.y_spacing * (len(self.buttons) + 1)
                top_y = (1/2) * int(settings["screen_height"]) - (1/2) * total_height

                button.rect.y = top_y + ((count + 1) * self.y_spacing) + \
                count * self.buttons[0].rect.height

            elif self.y_positioning == "bot":

                button.rect.y = int(settings["screen_height"]) - \
                (((len(self.buttons) - count) * self.y_spacing) + \
                (len(self.buttons) - count) * \
                button.rect.height)

            else:

                print("ERROR: INVALID Y AXIS POSITIONING")

            count += 1

        count = None
        return

    def display(self, surface):

        for button in self.buttons:

            button.display(surface)

        return

    def update(self):

        for button in self.buttons:

            button.update()

        return
