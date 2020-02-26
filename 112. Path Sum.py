# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if (not root.left and not root.right) and sum == root.val:
            return True

        sum -= root.val
        x = self.hasPathSum(root.left, sum)
        y = self.hasPathSum(root.right, sum)
        return x or y