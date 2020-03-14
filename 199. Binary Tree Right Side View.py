# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        ans = []
        queue = [(0, root)]
        curr = 0

        while queue:
            temp = queue.pop(0)
            if temp[0] != curr:
                ans.append(prev)
                curr = temp[0]
            if temp[1].left:
                queue.append((temp[0] + 1, temp[1].left))
            if temp[1].right:
                queue.append((temp[0] + 1, temp[1].right))

            prev = temp[1].val
        ans.append(prev)
        return ans