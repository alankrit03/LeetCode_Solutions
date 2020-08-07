# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        self.cache = {}

        def recur(node, rob=True):
            if not node:
                return 0

            if (node.val, rob) in self.cache:
                return self.cache[(node.val, rob)]

            if rob:
                x = node.val + recur(node.left, False) + recur(node.right, False)
                y = recur(node.left) + recur(node.right)
                curr = max(x, y)
            else:
                curr = recur(node.left) + recur(node.right)

            self.cache[(node.val, rob)] = curr
            return curr

        ans = recur(root)

        return ans