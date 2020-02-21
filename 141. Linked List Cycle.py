# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return 0

        s_ptr = head
        f_ptr = head

        while f_ptr and f_ptr.next:
            s_ptr = s_ptr.next
            f_ptr = f_ptr.next.next
            if s_ptr == f_ptr:
                return 1
