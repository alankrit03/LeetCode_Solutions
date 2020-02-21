# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0

        x = self.maxDepth(root.left)
        y = self.maxDepth(root.right)
        return 1 + max(x, y)