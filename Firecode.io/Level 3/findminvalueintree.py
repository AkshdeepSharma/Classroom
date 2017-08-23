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

    def find_min(self, root):
        current = self.root
        if current is None:
            return None
        while current.left_child:
            current = current.left_child
        return TreeNode(current)
