# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        ans = []
        if not root:
            return ans
        arr = []

        def paths(root):
            if not root:
                return
            arr.append(str(root.val))
            if not root.right and not root.left:
                ans.append('->'.join(arr))

            paths(root.left)
            paths(root.right)
            arr.pop()

        paths(root)
        return ans