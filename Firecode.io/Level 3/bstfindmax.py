class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' % self.data


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    # Iterative Solution
    def find_max(self, root):
        current = self.root
        if current is None:
            return None
        while current.right_child:
            current = current.right_child
        return TreeNode(current)

    # Recursive Solution
    def find_max1(self, root):
        if root is None:
            return None
        if root.right_child is None:
            return root
        return self.find_max(root.right_child)