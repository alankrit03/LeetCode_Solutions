# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.ans = 0

        def bintoint(x):
            n = 0
            for i in range(len(x)):
                n += int(x[i]) * 2 ** i
            return n

        def recur(node, s):
            if not node:
                return 0
            s = str(node.val) + s
            if (not node.left) and (not node.right):
                self.ans += bintoint(s)
                return

            if node.left:
                recur(node.left, s)
            if node.right:
                recur(node.right, s)

        recur(root, '')

        return self.ans