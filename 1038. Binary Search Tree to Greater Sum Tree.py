# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root: return root
        self.curr_sum = 0

        def change_val(root):
            if not root:
                return
            if not root.left and not root.right:
                root.val += self.curr_sum
                self.curr_sum = root.val
                return

            change_val(root.right)
            root.val += self.curr_sum
            self.curr_sum = root.val
            change_val(root.left)

        change_val(root)
        return root