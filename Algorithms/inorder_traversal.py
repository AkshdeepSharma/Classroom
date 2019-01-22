class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
