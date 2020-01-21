# Binary Tree implementation.
from sympy import preorder_traversal

from Code.Tree.BinaryTree.Node import Node


class BinaryTree:

    def __init__(self):
        print('***********************')
        print('***** BINARY TREE *****')
        print('***********************')
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_child(self, data):
        if not self.root.left:
            self.root.left = Node(data)
            return
        if self.root.left and not self.root.right:
            self.root.right = Node(data)
            return
        elif not self.root.left.left:
            self.root.left.left = Node(data)
            return
        elif not self.root.left.right:
            self.root.left.right = Node(data)

    def getroot(self):
        return self.root





