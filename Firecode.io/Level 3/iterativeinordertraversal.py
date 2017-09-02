class BinaryTree:
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def inorder_iterative(self):
        start = self
        inorder_list = []
        stack = []
        while stack or start:
            if start:
                stack.append(start)
                start = start.left_child
            else:
                item = stack.pop()
                inorder_list.append(item)
                start = item.right_child

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data
