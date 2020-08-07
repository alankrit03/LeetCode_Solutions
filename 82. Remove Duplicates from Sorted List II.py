# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        curr = None
        while head:
            if head.next:
                if head.val == head.next.val:
                    curr = head.val
            if curr == head.val:
                head = head.next
            else:
                break

        if not head:
            return

        ptr = head.next
        ptr1 = head
        curr = None

        while ptr:
            if ptr.next:
                if ptr.val == ptr.next.val:
                    curr = ptr.val
            if curr == ptr.val:
                ptr = ptr.next
            else:
                ptr1.next = ptr
                ptr1 = ptr1.next
                ptr = ptr.next
        ptr1.next = ptr
        return head
