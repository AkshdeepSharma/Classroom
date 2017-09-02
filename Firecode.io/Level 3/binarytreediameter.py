class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def diameter(self, root):
        return self.helper(self.root)[1]

    def helper(self, t):
        if not t:
            return 0, 0
        else:
            left_height, left_diameter = self.helper(t.left_child)
            right_height, right_diameter = self.helper(t.right_child)
            return max(left_height, right_height) + 1, max(left_diameter, right_diameter, left_height + right_height + 1)
