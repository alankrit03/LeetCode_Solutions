# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node, arr):
            if not node:
                return

            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)

        list1 = []
        list2 = []

        inorder(root1, list1)
        inorder(root2, list2)

        n = len(list1)
        m = len(list2)
        list1 += [0] * m

        idx = n + m - 1
        i = n - 1
        j = m - 1

        # print(list1)
        # print(list2)

        while i >= 0 and j >= 0:
            # print(list1[i],' __________ ',list2[j])
            if list1[i] > list2[j]:
                list1[idx] = list1[i]
                i -= 1
            else:
                list1[idx] = list2[j]
                j -= 1
            idx -= 1
            # print(list1,end='\n\n')
        else:
            if j > -1:
                list1[:j + 1] = list2[:j + 1]

        return list1