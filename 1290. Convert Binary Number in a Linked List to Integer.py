# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        self.ans = 0
        self.power = -1

        def recur(ptr):
            if not ptr:
                return

            recur(ptr.next)
            self.power += 1
            self.ans += ptr.val * (2 ** self.power)

        recur(head)

        return self.ans