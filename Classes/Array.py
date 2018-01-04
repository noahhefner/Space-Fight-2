# Noah Hefner
# Space Fight 2.0
# Alien Class
# Last Edit: 1/4/2018

class Array():
    """ Creates a matrix of points for menu item positioning. """

    def __init__ (self, screen_width, screen_height, rows, columns):
        """ Initiates Array class. """

        # TODO: Check if screen variables can be taken out of params and used
        #       from main function.

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rows = rows
        self.columns = columns

        self.array = []

        for i in range(self.rows):

            y = (i + 1) * (self.screen_height / (self.rows + 1))
            row = []

            for j in range(self.columns):

                x = (j + 1) * (self.screen_width / (self.columns + 1))

                position = [x,y]
                row.append(position)

            self.array.append(row)

        return

    def get_position(self, index_x, index_y):

        position = self.array[index_y - 1][index_x - 1]

        return position
