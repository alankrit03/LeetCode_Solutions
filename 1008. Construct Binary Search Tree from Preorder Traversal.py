# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        l, h = 0, len(preorder)

        """Using the binary search where the current first element in preorder should be.
        After finding it, divide the list into two part and that become the left and right node.
        All this happens recursively."""
        while h - l > 1:
            m = (l + h) // 2

            if preorder[0] >= preorder[m]:
                l = m
            else:
                h = m
        node = TreeNode(preorder[0])
        node.left = self.bstFromPreorder(preorder[1:h])
        node.right = self.bstFromPreorder(preorder[h:])

        return node