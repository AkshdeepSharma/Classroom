class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' % self.data


class BinaryTree:

    def __init__(self, root_node = None):
        self.root = root_node

    def find_min(self, root):
        if root is None:
            return None
        if root.left_child is None:
            return root
        return self.find_min(root.left_child)

    def delete(self, root, data):
        if root is None:
            return None
        elif data < root.data:
            root.left_child = self.delete(root.left_child, data)
        elif data > root.data:
            root.right_child = self.delete(root.right_child, data)
        else:
            if root.left_child is not None and root.right_child is not None:
                root.data = self.find_min(root.right_child).data
                root.right_child = self.delete(root.right_child, root.data)
            elif root.left_child is None and root.right_child is None:
                root = None
            elif root.left_child is None:
                root = root.right_child
            elif root.right_child is None:
                root = root.left_child
        return root
