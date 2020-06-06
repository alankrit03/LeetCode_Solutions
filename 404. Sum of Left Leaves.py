# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.ans = 0

        def recur(root):
            if not root:
                return

            if root.left and (not root.left.left and not root.left.right):
                self.ans += root.left.val

            recur(root.left)
            recur(root.right)

        recur(root)
        return self.ans