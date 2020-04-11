# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return

        ptr1 = head
        ptr2 = head2 = head.next

        while ptr1.next and ptr1.next.next:
            ptr1.next = ptr1.next.next
            ptr1 = ptr1.next

            if ptr1.next:
                ptr2.next = ptr1.next
                ptr2 = ptr2.next
            else:
                ptr2.next = None

        ptr1.next = head2
        return head