"""
Noah Hefner
Space Fight 2.0
Page Class
Last Edit: 6/29/2020
"""

class Page:

    def __init__ (self, id):

        self.id = id
        self.elements = []

    def add_element (self, new_element):

        self.elements.append(new_element)

    def display (self, screen):

        for element in self.elements:

            screen.blit(element.image, [element.rect.x, element.rect.y])
