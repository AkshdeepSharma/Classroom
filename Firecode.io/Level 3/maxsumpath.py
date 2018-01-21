class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def max_sum_path(self, root):
        return self.helper(root, 0)[1]

    def helper(self, root, curr_max):
        if root is None:
            return 0, curr_max
        l_down, l_max = self.helper(root.left_child, curr_max)
        r_down, r_max = self.helper(root.right_child, curr_max)

        return max(l_down, r_down) + root.data, max(l_max, r_max, curr_max, l_down + r_down + root.data)
