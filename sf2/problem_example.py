

class SomeClass:

    def __init__(self, function):

        self.function = function

    def do_function(self):

        self.function()

    ...

def modify_number(number):

    number += 3


number = 2
class_instance = SomeClass(modify_number(number))
