# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, wanted_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and wanted_sum == root.val:
            return True
        return self.hasPathSum(root.left, wanted_sum - root.val) or self.hasPathSum(root.right, wanted_sum - root.val)
