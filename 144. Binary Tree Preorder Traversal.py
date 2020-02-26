# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.list1 = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        # if not root.left and not root.right:
        #     self.list1.append(root.val)

        self.list1.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.list1