# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ptr = node

        while ptr.next.next:
            ptr.val, ptr.next.val = ptr.next.val, ptr.val
            ptr = ptr.next

        ptr.val, ptr.next.val = ptr.next.val, ptr.val
        ptr.next = None
