# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = float('-inf')

        def recur(node):
            if not node:
                return

            if not node.left and (not node.right):
                return (node.val, node.val)

            if node.left:
                min_, max_ = recur(node.left)

            if node.right:
                t1, t2 = recur(node.right)
                try:
                    min_ = min(min_, t1)
                    max_ = max(max_, t2)
                except:
                    min_ = t1
                    max_ = t2

            self.ans = max(self.ans, abs(min_ - node.val), abs(max_ - node.val))

            return (min(min_, node.val), max(max_, node.val))

        recur(root)
        return self.ans