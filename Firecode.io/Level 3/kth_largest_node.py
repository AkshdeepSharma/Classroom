class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    # Helper Method
    def size(self, root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child))

    def find_kth_largest(self, root, k):
        if root is None:
            return None

        size_right = 0

        if root.left_child:
            size_right = self.size(root.right_child)

        if size_right + 1 == k:
            return root
        elif k <= size_right:
            return self.find_kth_largest(root.right_child, k)
        else:
            return self.find_kth_largest(root.left_child, k - size_right - 1)