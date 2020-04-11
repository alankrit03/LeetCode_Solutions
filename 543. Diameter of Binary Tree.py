# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0

        def recur(node):
            if not node:
                return 0

            l = recur(node.left)
            r = recur(node.right)
            self.ans = max(self.ans, l + r)

            return max(l, r) + 1

        recur(root)

        return self.ans