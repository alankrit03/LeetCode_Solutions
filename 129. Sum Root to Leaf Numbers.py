# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0

        def recur(node, curr):
            if not node:
                return
            curr = curr * 10 + node.val
            if (not node.left) and (not node.right):
                self.ans += curr
                return

            if node.left:
                recur(node.left, curr)
            if node.right:
                recur(node.right, curr)

        recur(root, 0)
        return self.ans