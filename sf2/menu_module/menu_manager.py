
class MenuManager:

    def __init__ (self):

        self.pages = []
        self.current_page = None

    def navigate (self, page_id):

        for page in self.pages:

            if page.id == page_id:

                self.current_page = page

                return

    def update (self):

        for element in current_page.elements:

            pass

            # If element is clicked

                # Perform action function of element

                # return ?

    def display (self):

        self.current_page.display()
