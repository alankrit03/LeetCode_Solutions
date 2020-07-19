# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return

        queue = deque([(root, 0)])
        # print(queue)
        ans = []
        curr = 0
        tempArr = []
        while queue:
            temp = queue.popleft()
            if temp[1] == curr:
                tempArr.append(temp[0].val)
            else:
                if curr % 2:
                    ans.append(tempArr[::-1])
                else:
                    ans.append(tempArr)
                tempArr = [temp[0].val]
                curr = temp[1]

            if temp[0].left:
                queue.append((temp[0].left, temp[1] + 1))

            if temp[0].right:
                queue.append((temp[0].right, temp[1] + 1))

        if curr % 2:
            ans.append(tempArr[::-1])
        else:
            ans.append(tempArr)
        return ans