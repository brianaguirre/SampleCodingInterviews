__author__ = 'BrianAguirre'

from DataStructures.Lists.Itr import Itr
from DataStructures.Lists.Itr import Node


class List:

    node_list = []
    size = len(node_list) - 2

    head = Node()
    tail = Node()
    itr = Itr()

    node_list.append(head)
    node_list.append(tail)


    def __init__(self):
        self.length = 0
        self.itr.node = self.head
        self.head.next = self.tail
        self.tail.prev = self.head


    def insert_end(self, new_val):
        new_node = Node()
        new_node.data = new_val

        self.node_list.insert(self.size, new_node)
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node
        self.size += 1


    def insert_front(self, n):
        self.node_list.insert(0, n)



    #GET METHODS:

    def get_first(self):
        return self.head.next

    def get_last(self):
        return self.tail.prev

    def get_itr(self):
        return self.itr

    def move_itr_first(self):
        self.itr = self.head.next

    def move_itr_last(self):
        self.itr = self.tail.prev

    def print_list(self):
        self.move_itr_first()
        while self.itr.get_current_node() != self.tail:

            self.itr.node = self.itr.get_current_node()
            print(self.itr.get_current_node())

