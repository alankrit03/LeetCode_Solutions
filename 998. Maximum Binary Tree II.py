# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def recur(node, prev):
            if not node:
                prev.right = TreeNode(val)
                return

            if node.val < val:
                temp = TreeNode(val)
                temp.left = node
                prev.right = temp
                return
            recur(node.right, node)

        if not root:
            return TreeNode(val)

        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node

        recur(root.right, root)
        return root
