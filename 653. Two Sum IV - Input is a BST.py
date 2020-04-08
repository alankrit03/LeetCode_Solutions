# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = []

        def inorder(root, arr):
            if not root:
                return

            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

        inorder(root, arr)
        i, j = 0, len(arr) - 1

        while j - i > 0:
            if arr[i] + arr[j] == k:
                return True
            elif arr[i] + arr[j] > k:
                j -= 1
            else:
                i += 1
        return False
