# CREATE A SINGLY LINKED LIST OF NODES.
from .Node import Node


class LinkedList:

    def __init__(self):
        self.StartNode = None

    # Traverse through the node
    def traverse_through_node(self, position=None):
        node = self.StartNode
        if self.StartNode is None:
            print("Can't Traverse through an Empty List, Sorry :(")
            return
        elif position:
            print(str.format("Traversing to position {0}", position))
            for i in range(position-1):
                node = node.next_node
            return node
        else:
            print("Traversing to the last node")
            for i in range(self.length() + 1):
                if node.next_node.next_node is None:
                    return node
                node = node.next_node

    # Add a Node
    def add_node(self, data):
        node = Node()
        node.data = data
        self.StartNode = node
        return

    # Add a node at the beginning of the list.
    def add_node_at_starting(self, data):
        if self.StartNode is None:
            print("The Linked List is empty :(")
            return
        else:
            node = Node()
            node.data = data
            node.next_node = self.StartNode
            self.StartNode = node
            print(str.format("Node Successfully Added at the beginning with data = {0}", data))
            return

    # Add a node at the end of the list.
    def add_node_at_end(self, data):
        if self.StartNode is None:
            print("The Linked List is empty, cannot add data node at the end")
            return
        else:
            node = self.traverse_through_node()
            new_node = Node()
            new_node.data = data
            node.next_node.next_node = new_node
            new_node.next_node = None
            print(str.format("Node Successfully Added at the end with data = {0}", data))
            return

    # Add a node in between the list.
    def add_node_in_between(self, data, position):
        if self.StartNode is None:
            print(str.format("The Linked List is empty, cannot add data node at the position {0}", position))
            return
        else:
            prev_node = self.traverse_through_node(position)
            a = prev_node.next_node
            new_node = Node()
            new_node.next_node = a
            new_node.data = data
            prev_node.next_node = new_node
            print(str.format("Node Successfully Added at position {0} with data = {1}", position, data))
            return

    # Delete from the beginning of the list.
    def delete_start_node(self):
        if self.StartNode is None:
            print("The Linked List is empty, cannot delete from an empty List :(")
            return
        else:
            print(str.format("Start Node {0} is deleted", self.StartNode.data))
            self.StartNode = self.StartNode.get_next()
            return

    # Delete from the End of the list.
    def delete_end_node(self):
        if self.StartNode is None:
            print("The Linked List is empty, cannot delete from an empty list :(")
            return
        else:
            node = self.traverse_through_node()
            print(str.format("End Node with data {0} is deleted", node.next_node.data))
            node.set_node()

    # Delete from the middle of the list.
    def delete_node_at_position(self, position):
        if self.StartNode is None:
            print("The Linked List is empty, cannot delete from an empty list :(")
            return
        else:
            node = self.traverse_through_node(position)
            print(str.format("Node at position {1} with data {0} is deleted", node.next_node.data, position))
            node.next_node = node.next_node.next_node

    # Search Elements in the List.
    def search_list(self, data):
        print("\n... SEARCHING DATA ...")
        print(str.format("... Scanning for position of {0} in the list ...", data))
        if self.StartNode is None:
            print("The Linked List is empty :(")
            return
        else:
            if self.StartNode.data == data:
                print(str.format("{0} is at position 1", data))
            else:
                node = self.StartNode.next_node
                count = 2
                while node.next_node is not None:
                    if node.data == data:
                        print(str.format("{0} is at position {1}\n", data, count))
                        break
                    node = node.next_node
                    count += 1
            return

    # Return the Length of the list.
    def length(self):
        node = self.StartNode
        count = 0
        while node:
            count += 1
            node = node.next_node
        return count

    # Display the List
    def display(self):
        if self.StartNode is None:
            print("No data to display Linked List is empty :(")
            return
        else:
            node = self.StartNode
            data = []
            if node.next_node is None:
                data.append(node.data)
            while node.next_node is not None:
                if node.next_node.next_node is None:
                    data.append(node.data)
                    data.append(node.next_node.data)
                    node = node.next_node
                else:
                    data.append(node.data)
                    node = node.next_node
            print(data)
