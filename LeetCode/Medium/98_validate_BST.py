# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, lo=float('-inf'), hi=float('inf')) -> bool:
        if not root:
            return True
        if not lo < root.val < hi:
            return False
        return self.isValidBST(root.left, lo, min(root.val, hi)) and self.isValidBST(root.right, max(lo, root.val), hi)