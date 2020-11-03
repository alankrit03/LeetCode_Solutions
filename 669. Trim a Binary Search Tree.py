# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def DFS(root):
            if not root:
                return root

            if root.val < low:
                return DFS(root.right)
            elif root.val > high:
                return DFS(root.left)
            else:
                root.left = DFS(root.left)
                root.right = DFS(root.right)
            return root

        root = DFS(root)
        return root