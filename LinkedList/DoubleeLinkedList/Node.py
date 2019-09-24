"""Creating a node to implement Doublee Linked List"""


class Node:
    def __init__(self, data = None, next_node = None, prev_node = None):
        self.data = data
        self.prevNode = prev_node
        self.nextNode = next_node
