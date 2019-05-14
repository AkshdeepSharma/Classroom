"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res, stack = [], [root]
        if not root:
            return res
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]