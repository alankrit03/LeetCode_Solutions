# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        ptr = self.swapPairs(head.next.next)
        temp = head.next
        head.next = ptr
        temp.next = head
        return temp