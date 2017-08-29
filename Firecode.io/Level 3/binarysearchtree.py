class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' % self.data


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def insert(self, root, data):
        if root is None:
            root = TreeNode(data)
        elif data < root.data:
            root.left_child = self.insert(root.left_child, data)
        elif data > root.data:
            root.right_child = self.insert(root.right_child, data)
        return root

