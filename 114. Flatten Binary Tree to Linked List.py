# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def getRightMost(node):
            while node.right:
                node = node.right
            return node

        def recur(node):
            if not node:
                return

            if node.left:
                temp = getRightMost(node.left)
                temp.right = node.right
                node.right = node.left
                node.left = None

            recur(node.right)

        recur(root)

