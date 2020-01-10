# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        node = TreeNode(val)
        while True:
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = node
                    return root
            elif val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = node
                    return root