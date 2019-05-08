"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res, stack = [], root and [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(child for child in reversed(node.children) if child)
        return res