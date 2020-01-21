from Code.LinkedList.DoubleeLinkedList.LinkedList import DoubleeLinkedList


class Queue:

    def __init__(self):
        self.my_list = DoubleeLinkedList()

    def enque(self, data):
        if len(self.my_list) == 0:
            self.my_list.prepend(data)
        else:
            self.my_list.append(data)

    def deque(self):
        return self.my_list.delete(len(self.my_list))

    def peek(self):
        print(self.my_list.last())

    def is_empty(self):
        if len(self.my_list) == 0:
            return True
        else:
            return False

    def display(self):
        self.my_list.display()


