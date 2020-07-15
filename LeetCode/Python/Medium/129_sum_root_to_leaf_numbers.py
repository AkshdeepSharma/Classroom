# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, total):
        if root:
            self.dfs(root.left, total * 10 + root.val)
            self.dfs(root.right, total * 10 + root.val)
            if not root.left and not root.right:
                self.ans += total * 10 + root.val
