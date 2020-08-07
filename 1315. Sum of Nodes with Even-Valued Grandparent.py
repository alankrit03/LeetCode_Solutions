# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.values = [0] * 10 ** 4
        self.ans = 0

        def recur(node, level):
            if not node:
                return
            self.values[level] = node.val
            if level > 1:
                if self.values[level - 2] % 2 == 0:
                    self.ans += node.val

            recur(node.left, level + 1)
            recur(node.right, level + 1)

        recur(root, 0)
        return self.ans