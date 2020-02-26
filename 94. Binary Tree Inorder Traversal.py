# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.list1 = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        self.inorderTraversal(root.left)
        self.list1.append(root.val)
        self.inorderTraversal(root.right)

        return self.list1