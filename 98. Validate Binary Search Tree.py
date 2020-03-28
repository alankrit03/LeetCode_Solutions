# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = []

        def inorder(root, stack):
            if not root:
                return

            inorder(root.left, stack)
            stack.append(root.val)
            inorder(root.right, stack)

        inorder(root, stack)
        print(stack)
        max_ = max(stack)
        stack.pop()
        while stack:
            temp = stack.pop()
            if temp >= max_:
                return False
            max_ = temp

        return True