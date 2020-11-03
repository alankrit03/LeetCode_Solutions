# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def insert(ptr):
            if not ptr or (not ptr.next):
                return

            insert(ptr.next)

            while ptr.next and ptr.val > ptr.next.val:
                ptr.val, ptr.next.val = ptr.next.val, ptr.val
                ptr = ptr.next

        insert(head)
        return head