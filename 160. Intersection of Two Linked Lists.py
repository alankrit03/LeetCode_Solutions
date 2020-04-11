# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        change_a = change_b = False
        if not a or not b:
            return None
        while a != b:
            a = a.next
            b = b.next

            if not a:
                if change_a:
                    return None
                else:
                    a = headB
                    change_a = True

            if not b:
                if change_b:
                    return None
                else:
                    b = headA
                    change_b = True

        return a

