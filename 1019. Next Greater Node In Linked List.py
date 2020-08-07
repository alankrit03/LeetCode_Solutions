# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        stack = []
        result = []
        n = -1

        while head:
            result.append(0)
            n += 1

            while stack and stack[-1][0] < head.val:
                result[stack.pop()[1]] = head.val

            stack.append((head.val, n))
            head = head.next
        return result