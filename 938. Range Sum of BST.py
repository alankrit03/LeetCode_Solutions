# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0

        def recur(root):
            if not root:
                return

            if root.val > R:
                recur(root.left)
            elif root.val < L:
                recur(root.right)
            else:
                self.ans += root.val
                recur(root.left)
                recur(root.right)

        recur(root)
        return self.ans