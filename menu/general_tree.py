"""
Noah Hefner
Space Fight 2.0
General Tree Data Structure
Last Edit: 8/14/2019
"""


class Node:

    def __init__(self, data,  id):

        self.data = data
        self.id = id
        self.children = []  # List of nodes

    def add_child(self, child_node):

        self.children.append(child_node)

class Tree:

    def __init__(self):

        
