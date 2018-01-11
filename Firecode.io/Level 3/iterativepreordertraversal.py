class BinaryTree:
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder_iterative(self):
        start = self
        pre_ordered_List = []
        stack = []
        stack.append(start)
        while stack:
            item = stack.pop()
            pre_ordered_List.append(item)
            if item.right_child:
                stack.append(item.right_child)
            if item.left_child:
                stack.append(item.left_child)
        return pre_ordered_List

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data