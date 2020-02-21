# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1.val)
        arr1 = [str(l1.val)]
        arr2 = [str(l2.val)]

        while l1.next:
            l1 = l1.next
            arr1.insert(0, str(l1.val))

        while l2.next:
            l2 = l2.next
            arr2.insert(0, str(l2.val))

        value = int(''.join(arr1)) + int(''.join(arr2))

        result = ListNode(value % 10)
        value = value // 10

        ptr = result
        while value:
            ptr1 = ListNode(value % 10)
            ptr.next = ptr1
            value = value // 10
            ptr = ptr1

        # print(ptr1.val)

        return result