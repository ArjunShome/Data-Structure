# Creation of a Stack
from Code.LinkedList.SinglyLinkedList.LinkedList import LinkedList


class Stack:

    def __init__(self):
        self.length = 0
        self.top = None
        self.stack = LinkedList()

    def __len__(self):
        return self.length

    def push(self, data):
        if self.length == 0:
            self.stack.add_node(data)
        else:
            self.stack.add_node_at_end(data)
        self.length += 1
        node = self.stack.StartNode
        while node.next_node is not None:
            node = node.next_node
        self.top = node

    def pop(self):
        deleted_node = self.top
        self.stack.delete_end_node()
        if self.stack.StartNode == self.top:
            self.top = None
            return
        node = self.stack.StartNode
        while node.next_node is not None:
            node = node.next_node
        self.top = node
        self.length -= 1
        return deleted_node.data

    def peek(self):
        print(self.top)

    def is_empty(self):
        if self.length == 0:
            print("Empty")
            return
        print("Not Empty")
        return

    def is_full(self):
        if self.length == self.stack.length():
            print("Full")
            return
        print("Not Full")
        return

    def __len__(self):
        return self.length

    def display(self):
        self.stack.display()
