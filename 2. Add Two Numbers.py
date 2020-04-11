# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = None
        while l1 or l2:
            if l1 and l2:
                temp = l1.val + l2.val + carry
                if not head:
                    head = ListNode(temp % 10)
                    carry = temp // 10
                    ptr = head
                else:
                    ptr.next = ListNode(temp % 10)
                    carry = temp // 10
                    ptr = ptr.next
                l1 = l1.next
                l2 = l2.next

            elif l1:
                temp = l1.val + carry
                ptr.next = ListNode(temp % 10)
                carry = temp // 10
                ptr = ptr.next
                l1 = l1.next

            else:
                temp = l2.val + carry
                ptr.next = ListNode(temp % 10)
                carry = temp // 10
                ptr = ptr.next
                l2 = l2.next

        if carry:
            ptr.next = ListNode(carry)

        return head