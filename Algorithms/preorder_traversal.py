class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
