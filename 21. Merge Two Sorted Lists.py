# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:return l1
        if l1.val < l2.val:
            ptr = self.mergeTwoLists(l1.next , l2)
            l1.next = ptr
            return l1
        else:
            ptr = self.mergeTwoLists(l1 , l2.next)
            l2.next = ptr
            return l2