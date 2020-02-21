# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def print_list(ptr):
            while ptr:
                print(ptr.val)
                ptr = ptr.next

        def helper(fhead, head, m, n):
            if m == n:
                fhead.next = head.next
                return head
            ptr = head
            temp = head.next
            ptr.next = None
            head1 = helper(fhead, temp, m + 1, n)
            temp.next = ptr

            return head1

        ptr1 = None if m == 1 else head
        ptr2 = head

        for i in range(1, m - 1):
            ptr1 = ptr1.next
        temp1 = head if m == 1 else ptr1.next

        temp2 = helper(temp1, temp1, m, n)
        print_list(temp2)

        if m == 1:
            return temp2
        ptr1.next = temp2
        return head