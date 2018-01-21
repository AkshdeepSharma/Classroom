from collections import deque
import sys
class BinaryTree:
    def __init__(selfself, root_node = None):
        self.root = root_node

    def validate_BST_itr(selfself, root):

        stack = []

        if root:
            stack.append(root, -sys.maxint - 1, sys.maxint)

        while stack:
            node, lower, upper = stack.pop()
            if node.data > lower and node.data < upper:
                if node.left_child:
                    stack.append(node.left_child, lower, node.data)
                if node.right_child:
                    stack.append(node.right_child, node.data, upper)
            else:
                return False

        return True
