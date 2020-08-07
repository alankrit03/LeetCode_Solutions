# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val

        def recur(node):
            if not node:
                return True

            return node.val == value and recur(node.left) and recur(node.right)

        return recur(root)