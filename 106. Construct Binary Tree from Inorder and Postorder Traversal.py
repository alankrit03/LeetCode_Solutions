# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        if len(inorder)==1:
            return TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        n = len(inorder)
        l_tree = self.buildTree(inorder[:pos] , postorder[:pos])
        r_tree = self.buildTree(inorder[pos+1:], postorder[pos:n-1])
        node = TreeNode(postorder[-1])
        node.left = l_tree
        node.right = r_tree
        return node