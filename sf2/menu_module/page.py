
class Page:

    def __init__ (self, id):

        self.id = id
        self.elements = []

    def add_element (self, new_element):

        self.elements.append(new_element)

    def display (self):

        for element in self.elements:

            element.display()
