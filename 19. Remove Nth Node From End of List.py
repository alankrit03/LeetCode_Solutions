# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        s_ptr = head
        f_ptr = head

        while n:
            f_ptr = f_ptr.next
            n -= 1

        # print(f_ptr.val)
        if not f_ptr:
            head = head.next
        else:
            while f_ptr.next:
                f_ptr = f_ptr.next
                s_ptr = s_ptr.next
            # print(s_ptr.val)
            s_ptr.next = s_ptr.next.next

        return head