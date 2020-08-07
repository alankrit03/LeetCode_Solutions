# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def findleaf(node, arr):
            if not node:
                return

            if (not node.left) and (not node.right):
                arr.append(node.val)
                return

            findleaf(node.left, arr)
            findleaf(node.right, arr)

        leaf1 = []
        findleaf(root1, leaf1)
        leaf2 = []
        findleaf(root2, leaf2)

        return leaf1 == leaf2