class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
