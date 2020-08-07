# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2

        def recur(p1, p2):
            if p1 and p2:
                p1.val += p2.val
                if p1.left:
                    if p2.left:
                        recur(p1.left, p2.left)
                else:
                    p1.left = p2.left
                    p2.left = None

                if p1.right:
                    if p2.right:
                        recur(p1.right, p2.right)
                else:
                    p1.right = p2.right
                    p2.right = None

        recur(t1, t2)
        return t1