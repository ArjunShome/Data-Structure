"""
Circular Linked List implementation
"""
from Code.LinkedList.CircularLinkedList.Node import Node


class CircularLinkedList:
    _head = None
    _length = 0
    _current = None

    def _traverse(self, position=None):
        """
        Traverse the Circular Linked list
        :param position:
        :return:
        """
        try:
            node = self._head
            i = 0
            while True:
                node = node.next_node
                i += 1
                if position and position == i:
                    return node
                elif i == self._length:
                    break
            return node
        except Exception as ex:
            print(f"Failed Traversing List with error:- {ex}")

    def insert(self, data, position=None):
        """
        Insert node at:
        1. If position is not mentioned, adding the node as the head of the Circular Linked list
        2. If position is mentioned, Inserting node at that particular position.
        :param data:
        :param position:
        :return:
        """
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._head.next_node = self._head
            self._head.prev_node = self._head
            return
        if position:
            node = self._traverse(position=position)
            node.prev_node.next_node = new_node
            new_node.prev_node = node.prev_node
            node.prev_node = new_node
            new_node.next_node = node
            self._length += 1
            return
        new_node.next_node = self._head
        new_node.prev_node = self._head.prev_node
        self._head.prev_node.next_node = new_node
        self._head.prev_node = new_node
        self._head = new_node
        self._length += 1

    def append(self, data):
        """
        Adds a node to the Circular Linked list
        :param data:
        :return:
        """
        new_node = Node(data)
        node = self._traverse()
        self._head.prev_node = new_node
        node.next_node = new_node
        new_node.prev_node = node
        new_node.next_node = self._head
        self._length += 1

    def remove(self, data=None, position=None):
        """
        Removes a node fro the list,
        1. Remove node as per user input
        2. Remove node at position
        3. Remove the end Node
        :param data:
        :param position:
        :return:
        """
        if data:
            start_node = self._head
            current_node = start_node.next_node
            while True:
                if start_node.data == data:
                    start_node.prev_node.next_node = self._head.next_node
                    start_node.next_node.prev_node = self._head.prev_node
                    self._head = start_node.next_node
                    self._length -= 1
                    return
                if current_node.data == data:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    current_node = current_node.next_node
                    self._length -= 1
                if current_node == self._head:
                    return
                current_node = current_node.next_node
        elif position:
            node = self._traverse(position=position)
        else:
            node = self._traverse()
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        self._length -= 1

    def __len__(self):
        """
        Gets the length of the Linked List
        :return: length
        """
        return self._length

    def display(self):
        """
        Display the Circular List
        :return: list o Data present in the circular linked list
        """
        current_node = self._head
        data = []
        while True:
            data.append(current_node.data)
            current_node = current_node.next_node
            if current_node == self._head:
                break
        print(data)
