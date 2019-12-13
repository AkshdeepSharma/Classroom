import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum, best_level, curr_level = float('-inf'), 0, 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr_level += 1
            curr_sum = 0
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                curr_sum += curr_node.val
            if curr_sum > max_sum:
                max_sum = curr_sum
                best_level = curr_level
        return best_level
