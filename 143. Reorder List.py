# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
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
                ptr=head
                temp=head.next
                ptr.next = None
                head1 = reverse(temp)
                temp.next = ptr

                return head1

            head2 = mid_head(head)
            head2 = reverse(head2)
            ptr = head

            while head2:
                temp = head2
                head2 = head2.next
                ptr2 = ptr.next
                ptr.next = temp
                temp.next = ptr2
                ptr = ptr2


