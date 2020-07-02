"""
Noah Hefner
Space Fight 2.0
Page Class
Last Edit: 6/29/2020
"""


class Page:
    """
    Page object for menu manager.

    Attributes:
        id (string/int): ID for this page.
        elements (List): List of elements on the page.

    NOTE: The ID doesn't have to be a string/int, it just has to be some
          distinct identifier for this page. I just recommend using a string or
          an integer for simplicity and readability.
    """

    def __init__ (self, id):
        """
        Instantiate a page object.

        Arguments:
            id (string/int): ID for this page.
        """

        self.id = id
        self.elements = []

    def add_element (self, new_element):
        """
        Adds an element to the page.

        Arguments:
            new_element (Button): Element to add to the page.
        """

        self.elements.append(new_element)

    def display (self, screen):
        """
        Show this screen in the window.

        Arguments:
            screen (pygame.display): Surface to blit the elements to.
        """

        for element in self.elements:

            screen.blit(element.image, [element.rect.x, element.rect.y])
