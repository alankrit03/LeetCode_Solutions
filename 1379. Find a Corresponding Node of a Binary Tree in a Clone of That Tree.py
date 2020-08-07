# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def recur(node, x):
            if not node:
                return

            if node.val == x.val:
                self.ans = node
                return

            recur(node.left, x)
            recur(node.right, x)

        recur(cloned, target)
        return self.ans