# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, side=None):
            if not node:
                return

            if not node.left and (not node.right):
                if node is root:
                    return
                if side == 'left':
                    self.ans += node.val
                return

            dfs(node.left, 'left')
            dfs(node.right, 'right')

        dfs(root)
        return self.ans
