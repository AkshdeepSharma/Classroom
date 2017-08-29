class BinaryTree:
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def inorder_iterative(self):
        inorder_list = []
        stack = []
        while True:
            while self is not None:
                stack.append(self)
                self = self.get_left_child()
            if stack is []:
                break
            else:
                self = stack.pop()
                inorder_list.append(self.data)
                self = self.get_right_child()
        return inorder_list

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data
