# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        return self.inorder(root, 0, L, R)

    def inorder(self, root, value, L, R):
        if root:
            value = self.inorder(root.left, value, L, R)
            if root.val >= L and root.val <= R:
                value += root.val
            value = self.inorder(root.right, value, L, R)
        return value