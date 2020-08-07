# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inorder = []
        if not root:
            return

        def recur(root):
            if not root:
                return

            recur(root.left)
            self.inorder.append(root.val)
            recur(root.right)

        recur(root)

        head = TreeNode(self.inorder[0])
        ptr = head

        for i in range(1, len(self.inorder)):
            ptr.right = TreeNode(self.inorder[i])
            ptr = ptr.right

        return head