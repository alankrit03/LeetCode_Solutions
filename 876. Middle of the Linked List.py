# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s_ptr = head
        f_ptr = head

        while f_ptr and f_ptr.next:
            f_ptr = f_ptr.next.next
            s_ptr = s_ptr.next

        return s_ptr