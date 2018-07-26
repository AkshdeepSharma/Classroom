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

    def get_node_distance(self, root, node_data1, node_data2):

        if not self.root:
            return 0

        def dfs(target):
            stack = [(root, [root])]
            while stack:
                current, path = stack.pop()
                if current.data == target:
                    return path
                if current.left_child:
                    stack.append((current.left_child, path + [current.left_child]))
                if current.right_child:
                    stack.append((current.right_child, path + [current.right_child]))
            return []

        node1_path = dfs(node_data1)
        node2_path = dfs(node_data2)
        common = 0
        for a, b in zip(node1_path, node2_path):
            if a.data != b.data:
                break
            common += 1
        return len(node1_path) + len(node2_path) - 2 * common
