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

    # Helper Method
    def size(self, root):
        if root is None:
            return 0
        else:
            return self.size(root.left_child) + 1 + self.size(root.right_child)

    def find_kth_smallest(self, root, k):
        if root is None:
            return None

        size_left = 0

        if not root.left_child:
            size_left = self.size(root.left_child)

        if size_left + 1 == k:
            return root
        elif k <= size_left:
            return self.find_kth_smallest(root.left_child, k)
        else:
            return self.find_kth_smallest(root.right_child, k - size_left - 1)