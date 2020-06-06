# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def sortedArrayToBST(nums: List[int]) -> TreeNode:
            if not nums:
                return

            mid = len(nums) // 2

            node = TreeNode(nums[mid])
            node.left = sortedArrayToBST(nums[:mid])
            node.right = sortedArrayToBST(nums[mid + 1:])
            return node

        return sortedArrayToBST(arr)
