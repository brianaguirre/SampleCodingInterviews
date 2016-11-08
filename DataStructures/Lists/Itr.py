__author__ = 'BrianAguirre'

from DataStructures.Lists.Node import Node

class Itr(object):

    node = Node()
    next_node = None
    prev_node = None

    def __init__(self):
        self.node = Node()
        self.next_node = Node()
        self.prev_node = Node()

    def move_right(self):
        self.node = self.node.get_next()
        self.next_node = self.node.next
        self.prev_node = self.prev_node

    def move_left(self):
        self.node = self.node.get_prev()
        self.next_node = self.node.next
        self.prev_node = self.node.prev

    def get_current_node(self):
        return self.node






