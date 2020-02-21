# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ptr = head
        temp = head.next
        ptr.next = None
        head1 = self.reverseList(temp)
        temp.next = ptr

        return head1