# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr1 = ptr
                while ptr1 and ptr1.val == ptr.val:
                    ptr1 = ptr1.next
                ptr.next = ptr1
            ptr = ptr.next
        return head