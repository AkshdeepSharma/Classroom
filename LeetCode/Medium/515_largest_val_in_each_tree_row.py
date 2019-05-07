# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        queue = []
        res = []
        max_list = []
        height = 0
        queue.append((height, root))
        while (len(queue) > 0):
            node = queue.pop(0)
            if node[0] != height:
                height = node[0]
                res.append(max(max_list))
                max_list = []
            max_list.append(node[1].val)
            if node[1].left:
                queue.append((node[0] + 1, node[1].left))
            if node[1].right:
                queue.append((node[0] + 1, node[1].right))

        return res + [max(max_list)]