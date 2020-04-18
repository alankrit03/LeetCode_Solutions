# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            n += 1

        if n < 2:
            return head

        k = k % n
        if not k:
            return head

        fptr = head
        while k:
            fptr = fptr.next
            k -= 1

        ptr = head
        while fptr.next:
            fptr = fptr.next
            ptr = ptr.next

        new_head = ptr.next
        ptr.next = None
        fptr.next = head
        return new_head