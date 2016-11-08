__author__ = 'BrianAguirre'

from DataStructures.Lists.List import List

#TESTING OUT LIST, NODE, ITR CLASSES:

my_list = List()

my_list.insert_end(1)
my_list.insert_end(2)

print(my_list.tail.prev.data)
print(my_list.tail.prev.prev.data)


my_list.print_list()





