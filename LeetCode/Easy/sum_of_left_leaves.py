# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        if root is None or (root.left is None and root.right is None):
            return 0
        self.helper(root, res)
        return sum(res)

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            if root.right and (root.right.right is not None or root.right.left is not None):
                self.helper(root.right, res)
            if root.left is None and root.right is None:
                res.append(root.val)