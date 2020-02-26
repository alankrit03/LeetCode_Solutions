# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.list1 = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.list1.append(root.val)

        return self.list1