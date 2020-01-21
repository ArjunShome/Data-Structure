""" Implementing the Doublee linked list """

from .Node import Node


class DoubleeLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Length = 0

    """ Adding a node to the list at the beginning """
    def prepend(self, data):
        node = Node(data)
        if self.Length == 0:
            self.head = node
            self.tail = self.head
            self.Length += 1
            #print(str.format("Adding Node {0} at the beginning of the list", node.data))
            return
        node.nextNode = self.head
        self.head.prevNode = node
        self.head = node
        self.Length += 1
        print(str.format("Adding Node {0} at the beginning of the list", node.data))

    def append(self, data):
        node = Node(data)
        if self.Length == 0:
            node = Node(data)
            self.tail = node
            self.head = self.tail
            self.Length += 1
            #print(str.format("Adding Node {0} at the end of the list", node.data))
            return
        node.prevNode = self.tail
        self.tail.nextNode = node
        self.tail = node
        self.Length += 1
        #print(str.format("Adding Node {0} at the end of the list", node.data))

    def insert(self, data, position):
        node = Node()
        node.data = data
        if self.Length < position:
            return print(str.format("The length of the list is less than the supplied position Length: {0}, position \
            to be inserted: {1}", self.Length, position))
        elif position == 1:
            node.prevNode = None
            node.nextNode = self.head
            self.head = node
            return
        elif self.Length == position:
            node.prevNode = self.tail.prevNode
            node.nextNode = self.tail
            self.tail.prevNode.nextNode = node
            self.tail.prevNode = node
            self.Length += 1
            return
        dummy_head = self.head
        for p in range(position - 1):
            dummy_head = dummy_head.nextNode
        node.nextNode = dummy_head
        node.prevNode = dummy_head.prevNode
        dummy_head.prevNode.nextNode = node
        dummy_head.prevNode = node
        self.Length += 1

    def delete(self, position):
        if self.Length < position:
            print('Position provided for the element in the queue to delete is out of bound')
            return
        elif position == 1:
            dummy_head = self.head
            self.head = self.head.nextNode
            self.tail = self.head
            self.Length -= 1
            return dummy_head
        elif self.Length == position:
            dummy_tail = self.head
            self.head = self.head.nextNode
            self.head.prevNode = None
            self.Length -= 1
            return dummy_tail
        dummy_head = self.head
        delete_node = None
        for p in range(position - 1):
            delete_node = dummy_head.nextNode
            dummy_head = dummy_head.nextNode
        delete_node.nextNode.prevNode = delete_node.prevNode
        delete_node.prevNode.nextNode = delete_node.nextNode
        return delete_node

    def pop(self):
        if self.Length == 0:
            print("No Items in the List to Delete :(")
            return
        if self.Length == 1:
            self.head = None
            self.tail = None
            return
        self.head = self.head.nextNode
        self.head.prevNode = None
        self.Length -= 1

    def __len__(self):
        return self.Length

    def display(self):
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

    def search(self, data):
        if self.Length == 0:
            return print("Nothing to Search, The List is empty.")
        dummy_head = self.head
        location = 0
        while dummy_head is not None:
            if dummy_head.data == data:
                print(str.format("{0} is at postion: {1}", data, location))
                return
            dummy_head = dummy_head.nextNode
            location += 1

    def last(self):
        dummy_head = self.head
        while dummy_head.nextNode is not None:
            dummy_head = dummy_head.nextNode
        return dummy_head.data

