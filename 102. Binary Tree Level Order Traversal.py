# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        list1 = [[]]
        curr = 0
        queue = [(root, 0)]

        while queue:
            temp = queue[0][0]
            if curr != queue[0][1]:
                list1.append([])
                curr += 1
            list1[-1].append(temp.val)
            queue.pop(0)
            if temp.left:
                queue.append((temp.left, curr + 1))
            if temp.right:
                queue.append((temp.right, curr + 1))

        return list1
