# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def recur(node, p, q):
            if not node:
                return False

            x = recur(node.left, p, q)
            y = recur(node.right, p, q)

            if x and y:
                self.ans = node
                return False
            if (x or y) and (node.val == p.val or node.val == q.val):
                self.ans = node
                return False

            if node.val == p.val or node.val == q.val:
                return True

            return x or y

        recur(root, p, q)

        return self.ans
