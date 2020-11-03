# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        ptr = head
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next

        arr.sort()
        ptr = head
        for x in arr:
            ptr.val = x
            ptr = ptr.next

        return head