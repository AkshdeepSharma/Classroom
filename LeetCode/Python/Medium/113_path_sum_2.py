# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, wanted_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(root, wanted_sum, [], ans)
        return ans

    def dfs(self, root, wanted_sum, temp, ans):
        if not root:
            return
        if not root.left and not root.right and wanted_sum == root.val:
            ans.append(temp + [root.val])
            return
        self.dfs(root.left, wanted_sum - root.val, temp + [root.val], ans)
        self.dfs(root.right, wanted_sum - root.val, temp + [root.val], ans)
