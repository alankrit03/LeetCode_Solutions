# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0

        def recur(node):
            if not node:
                return 0

            lsum = recur(node.left)
            rsum = recur(node.right)

            self.ans += abs(lsum - rsum)
            return lsum + rsum + node.val

        recur(root)
        return self.ans