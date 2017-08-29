class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def diameter(self, root):
        return self.diameter_helper_method(root, BinaryTree.Height())

    class Height:
        def __init__(self, h=0):
            self.h = h

    def diameter_helper_method(self, root, height):
        left_height = BinaryTree.Height()
        right_height = BinaryTree.Height()
        if root is None:
            height.h = 0
            return 0
        left_height.h += 1
        right_height.h += 1
        left_diameter = self.diameter_helper_method(root.left_child, left_height)
        right_diameter = self.diameter_helper_method(root.right_child, right_height)
        height.h = max(left_height.h, right_height.h) + 1
        return max(left_height.h + right_height.h + 1, max(left_diameter, right_diameter))


