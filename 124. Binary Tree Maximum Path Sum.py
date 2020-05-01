# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = -10 ** 7

        def recur(node):
            if not node:
                return 0

            x = max(recur(node.left), 0)
            y = max(recur(node.right), 0)

            self.ans = max((x + y + node.val), (x + node.val), (y + node.val), self.ans)

            return node.val + max(x, y)

        recur(root)

        return self.ans