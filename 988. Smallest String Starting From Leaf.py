# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import string


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        letters = string.ascii_lowercase
        self.ans = None

        def recur(node, s):
            if not node:
                return
            s = letters[node.val] + s
            if not node.left and (not node.right):
                if self.ans:
                    self.ans = min(self.ans, s)
                else:
                    self.ans = s

            if node.left:
                recur(node.left, s)

            if node.right:
                recur(node.right, s)

        recur(root, '')
        return self.ans