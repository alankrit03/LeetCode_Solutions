# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        if len(inorder) == 1:
            return TreeNode(preorder[-1])

        pos = inorder.index(preorder[0])
        n = len(inorder)
        l_tree = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        r_tree = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
        node = TreeNode(preorder[0])
        node.left = l_tree
        node.right = r_tree
        return node