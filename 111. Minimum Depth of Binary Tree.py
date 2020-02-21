# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root :return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            x = self.minDepth(root.left)
            y = self.minDepth(root.right)
            return 1+min(x,y)
        elif root.left:
            return 1+self.minDepth(root.left)
        else:
            return 1+self.minDepth(root.right)