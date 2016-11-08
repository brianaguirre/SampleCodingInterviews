__author__ = 'BrianAguirre'


#Class is inherited from Object class
class Node(object):

    data = int
    next = None
    prev = None

    def __init__(self):
        self.data = None


    #SET METHODS:
    def set_next(self, next_node):
        self.next = next_node

    def set_prev(self, prev_node):
        self.prev = prev_node


    #GET METHODS:

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev


    #POSSIBLY IN ITERATOR:


