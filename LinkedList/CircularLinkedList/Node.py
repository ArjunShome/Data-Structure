"""
Class which specifies the node definition.
"""


class Node:
    def __init__(self, node_data=None):
        self.data = node_data
        self.next_node = None
        self.prev_node = None
