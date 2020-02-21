# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        def mid_head(head):
            s_ptr = head
            f_ptr = head
            while f_ptr and f_ptr.next:
                f_ptr = f_ptr.next.next
                temp = s_ptr
                s_ptr = s_ptr.next

            if f_ptr:
                temp = s_ptr.next
                s_ptr.next = None
                return temp

            temp.next = None
            return s_ptr

        def reverse(head):
            if not head or not head.next:
                return head
            ptr = head
            temp = head.next
            ptr.next = None
            head1 = reverse(temp)
            temp.next = ptr

            return head1

        head2 = mid_head(head)
        head2 = reverse(head2)

        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True