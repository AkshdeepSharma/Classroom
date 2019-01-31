'''
    Based on the definition of balanced applying only to leaf nodes.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)

            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1

    def isBalanced(self, root):
        return abs(self.maxDepth(root) - self.minDepth(root)) <= 1
