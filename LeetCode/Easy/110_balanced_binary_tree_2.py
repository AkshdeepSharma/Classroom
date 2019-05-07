'''
    Based on the definition of balanced applying to root nodes as well.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.d = {}

    def isBalanced(self, root):
        def depth(root):
            if root is None:
                return 0
            if root in self.d:
                return self.d[root]
            self.d[root] = 1 + max(depth(root.left), depth(root.right))
            return self.d[root]

        if root is None:
            return True
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
            root.right)
