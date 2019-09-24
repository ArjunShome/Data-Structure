""" Implementing the Doublee linked list """

from .Node import Node


class DoubleeLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Length = 0
        self.lst = []

    """ Adding a node to the list at the beginning """
    def insert_beginning(self, data):
        node = Node(data)
        if self.Length == 0:
            self.head = node
            self.tail = self.head
            self.Length += 1
            self.lst.insert(self.Length - self.Length, node.data)
            print(str.format("Adding Node {0} at the beginning of the list", node.data))
            return
        node.nextNode = self.head
        self.head.prevNode = node
        self.head = node
        self.Length += 1
        self.lst.insert(self.Length - self.Length, node.data)
        print(str.format("Adding Node {0} at the beginning of the list", node.data))

    def insert_end(self, data):
        node = Node(data)
        if self.Length == 0:
            node = Node(data)
            self.tail = node
            self.head = self.tail
            self.Length += 1
            self.lst.insert(self.Length, node.data)
            print(str.format("Adding Node {0} at the end of the list", node.data))
            return
        node.prevNode = self.tail
        self.tail.nextNode = node
        self.tail = node
        self.Length += 1
        self.lst.insert(self.Length, node.data)
        print(str.format("Adding Node {0} at the end of the list", node.data))

    def insert_node(self, data, position, node):
        dummy_head = self.head
        for p in range(position - 1):
            dummy_head = dummy_head.nextNode
        node.nextNode = dummy_head
        node.prevNode = dummy_head.prevNode
        dummy_head.prevNode.nextNode = node
        dummy_head.prevNode = node
        node.data = data

    def insert_at_position(self, data, position):
        if self.Length < position:
            return print(str.format("The length of the list is less than the supplied position Length: {0}, position to be inserted: {1}", self.Length, position))
        elif self.Length == position:
            node = Node(1)
            node.data = data
            self.insert_node(data, position, node)
            self.Length += 1
            self.lst.insert(self.Length, node.data)
            return print(str.format("Adding Node {0} at position {1} of the list", node.data, position))
        node = Node()
        node.data = data
        self.insert_node(data, position, node)
        self.Length += 1
        self.lst.insert(self.Length, node.data)
        print(str.format("Adding Node {0} at position {1} of the list", node.data, position))

    def delete_node(self, position):
        dummy_head = self.head
        for p in range(position - 1):
            dummy_head = dummy_head.nextNode
        if dummy_head.nextNode is None:
            dummy_head.prevNode.nextNode = None
            dummy_head.prevNode = None
        dummy_head.nextNode.prevNode = dummy_head.prevNode
        dummy_head.prevNode.nextNode = dummy_head.nextNode
        return print(str.format("Deleting Node {0} at position {1} of the list", dummy_head.data, position))

    def delete_at_position(self, data, position):
        if self.Length < position:
            return print(str.format("The length of the list is less than the supplied position Length: {0}, position to be deleted: {1}", self.Length, position))
        self.delete_node(position)

    def delete_beginning(self):
        if self.Length == 0:
            print("No Items in the List to Delete :(")
            return
        if self.Length == 1:
            print(str.format("Removing the First Node {0}", self.head.data))
            self.lst.remove(self.head.data)
            self.head = None
            self.tail = None
            return
        print(str.format("Removing the First Node {0}", self.head.data))
        self.lst.remove(self.head.data)
        self.head = self.head.nextNode
        self.head.prevNode = None
        self.Length -= 1

    def delete_end(self):
        if self.Length == 0:
            print("No Items in the List to Delete :(")
            return
        if self.Length == 1:
            print(str.format("Removing the Last Node {0}", self.tail.data))
            self.lst.remove(self.tail.data)
            self.tail = None
            self.head = None
            return
        print(str.format("Removing the Last Node {0}", self.tail.data))
        self.lst.remove(self.tail.data)
        self.tail = self.tail.prevNode
        self.tail.nextNode = None
        self.Length -= 11

    def __len__(self):
        return self.Length

    def display(self):
        print("Printing the Linked List")
        if self.head is None:
            print("No data to display Linked List is empty :(")
            return
        else:
            node = self.head
            data = []
            if node.nextNode is None:
                data.append(node.data)
            while node.nextNode is not None:
                if node.nextNode.nextNode is None:
                    data.append(node.data)
                    data.append(node.nextNode.data)
                    node = node.nextNode
                else:
                    data.append(node.data)
                    node = node.nextNode
            print(data)
