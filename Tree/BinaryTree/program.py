from Code.Tree.BinaryTree.BinaryTree import BinaryTree
from Code.Stack.Incremental_Array_Stack.Stack import Stack
from Code.Queue.queue import Queue


class Order:

    # RECURSIVE TRAVERSALS
    def rec_preorder_traversal(self, root):
        if root is None:
            return
        print(root.data)
        self.rec_preorder_traversal(root.left)
        self.rec_preorder_traversal(root.right)

    def rec_inorder_traversal(self, root):
        if root is None:
            return
        self.rec_inorder_traversal(root.left)
        print(root.data)
        self.rec_inorder_traversal(root.right)

    def rec_postorder_traversal(self, root):
        if root is None:
            return
        self.rec_postorder_traversal(root.left)
        self.rec_postorder_traversal(root.right)
        print(root.data)

    # NON RECURSIVE TRAVERSALS

    def preorder_traversal(self, root):
        stack = Stack()
        while 1:
            while root:
                print(root.data)
                stack.push(root)
                root = root.left
            if not stack:
                break
            root = stack.pop()
            root = root.right

    def inorder_traversal(self, root):
        stack = Stack()
        while 1:
            while root:
                stack.push(root)
                root = root.left
            if not stack:
                break
            root = stack.pop()
            print(root.data)
            root = root.right

    def postorder_traversal(self, root):
        traversed_stack = Stack()
        stack = Stack()
        while root:
            if not stack and traversed_stack:
                while traversed_stack:
                    print(traversed_stack.pop().data)
                return
            if not stack and not traversed_stack:
                stack.push(root)
            current = stack.pop()
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            traversed_stack.push(current)

    def levelorder_traversal(self, root):
        queue = Queue()
        queue.enque(root)
        while not queue.is_empty():
            node = queue.deque()
            print(node.data.data)
            if node.data.left:
                queue.enque(node.data.left)
            if node.data.right:
                queue.enque(node.data.right)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert_root(10)
    tree.insert_child(20)
    tree.insert_child(30)
    tree.insert_child(40)
    tree.insert_child(50)
    root = tree.getroot()

    ord = Order()
    print('\nPRINTING PREORDER TRAVERSED DATA')
    ord.rec_preorder_traversal(root)
    print('\nPRINTING INORDER TRAVERSED DATA')
    ord.rec_inorder_traversal(root)
    print('\nPRINTING POSTORDER TRAVERSED DATA')
    ord.rec_postorder_traversal(root)
    print('\nPRINTING PREORDER TRAVERSED DATA NON RECURSIVE')
    ord.preorder_traversal(root)
    print('\nPRINTING INORDER TRAVERSED DATA NON RECURSIVE')
    ord.inorder_traversal(root)
    print('\nPRINTING POSTORDER TRAVERSED DATA NON RECURSIVE')
    ord.postorder_traversal(root)
    print('\nPRINTING LEVEL-ORDER TRAVERSED DATA NON RECURSIVE')
    ord.levelorder_traversal(root)
