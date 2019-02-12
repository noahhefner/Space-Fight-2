

class MenuPage():

    def __init__(self, name = "UNNAMED"):

        self.name = name
        self.text_buttons = []
        self.image_buttons = []

        self.x_spacing = 10
        self.y_spacing = 10
        self.x_positioning = "left"
        self.y_positioning = "top"

    def set_x_positioning(self, x_positioning):

        self.x_positioning = x_positioning

    def set_y_positioning(self, y_positioning):

        self.y_positioning = y_positioning

    def add_text_button(self, button):

        self.text_buttons.append(button)

        # Readjust coordinates for the buttons every time we add a button
        self.__set_coords()

    def add_image_button(self, image_button):

        self.image_buttons.append(image_button)

    def __set_coords(self):

        # Set x coordinates for all the buttons
        for i in range(len(self.text_buttons) - 1):

            if self.x_positioning == "left":

                for button in self.text_buttons:

                    button.rect.x = x_spacing

            elif self.x_positioning == "mid":

                for button in self.text_buttons:

                    button.rect.x = (Constants.SCREEN_WIDTH / 2) - \
                    (button.rect.width / 2)

            elif self.x_positioning == "right":

                for button in self.text_buttons:

                    button.rect.x = Constants.SCREEN_WIDTH - \
                    self.x_spacing - button.rect.width

            else

                print("Invalid x axis positioning")

        # Set y coordinates for all the buttons
        for i in range(len(self.text_buttons) - 1):

            if self.y_positioning = "top":

                for button in self.text_buttons:

                    button.rect.y = ((i + 1) * self.y_spacing) + \
                    i * self.text_buttons[0].rect.height

            elif self.y_positioning = "mid":

                # Calculations for mid positioning
                total_height = self.text_buttons[0].rect.height * \
                len(self.text_buttons) + \
                self.y_spacing * (len(self.text_buttons) + 1)
                top_y = (1/2) * Constants.SCREEN_HEIGHT - (1/2) * total_height

                for button in self.text_buttons:

                    button.rect.y = top_y + ((i + 1) * self.y_spacing) + \
                    i * self.text_buttons[0].rect.height

            elif self.y_positioning = "bot":

                for button in self.text_buttons:

                    button.rect.y.rect.y = \
                    ((len(self.text_buttons) + 1 - i) * self.y_spacing) + \
                    (len(self.text_buttons) - i) * \
                    self.text_buttons[0].rect.height

            else

                print("Invalid y axis positioning")

    def show_page(self, surface):

        for text_button in self.text_buttons:

            text_button.display(surface)

        for image_button in self.image_buttons:

            image_button.display(surface)
