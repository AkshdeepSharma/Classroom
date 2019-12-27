# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.inorder_traversal(root, res)
        min_difference = float("inf")
        for i in range(1, len(res)):
            min_difference = min(min_difference, res[i] - res[i - 1])
        return min_difference

    def inorder_traversal(self, root, res):
        if root:
            self.inorder_traversal(root.left, res)
            res.append(root.val)
            self.inorder_traversal(root.right, res)