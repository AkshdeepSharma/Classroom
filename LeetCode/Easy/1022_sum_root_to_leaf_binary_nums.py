# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorder(self, root, binary, res):
        if root:
            binary += str(root.val)
            self.preorder(root.left, binary, res)
            self.preorder(root.right, binary, res)
            if not root.left and not root.right:
                res.append(binary)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        max_int = 10 ** 9 + 7
        binary = ''
        dec = 0
        self.preorder(root, binary, res)
        for binary_num in res:
            num = int(binary_num, 2)
            dec += num
        return dec % max_int