# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return 1
        self.ans = 0

        def recur(node):
            if not node:
                return 0

            l = recur(node.left)
            r = recur(node.right)
            self.ans = max(self.ans, abs(l - r))

            return max(l, r) + 1

        recur(root)
        # print(self.ans)
        if self.ans <= 1:
            return True

        return False