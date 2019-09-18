# Implementing a Singly linked List
# Class Node having the node characteristics.


class Node:
    """ Initialize method To initialize dat and next node address """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    """ Method to get data """
    def get_data(self):
        return self.data

    """ Method to get node """
    def get_next(self):
        return self.next_node

    """ Method to set node """
    def set_node(self, new_next_node=None):
        self.next_node = new_next_node

    """ Method to check if the node is a last node. """
    def is_last_node(self):
        if self.next_node is None:
            return True
