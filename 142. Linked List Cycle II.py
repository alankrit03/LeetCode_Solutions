# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def hasCycle(head):
            if not head or not head.next:
                return None

            s_ptr = head
            f_ptr = head

            while f_ptr and f_ptr.next:
                s_ptr = s_ptr.next
                f_ptr = f_ptr.next.next
                if s_ptr == f_ptr:
                    return s_ptr

        temp = hasCycle(head)
        if not temp:
            return temp

        ptr = head

        while ptr != temp:
            ptr = ptr.next
            temp = temp.next

        return ptr