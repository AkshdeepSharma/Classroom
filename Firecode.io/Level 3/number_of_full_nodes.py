from collections import deque
class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    # Required collection modules have already been imported.
    def number_of_full_nodes(self, root):
        count = 0
        if root is None:
            return count
        queue = deque()
        queue.append(root)
        while queue:
            item = queue.popleft()
            if item.left_child and item.right_child:
                count += 1
            if item.left_child:
                queue.append(item.left_child)
            if item.right_child:
                queue.append(item.right_child)
        return count