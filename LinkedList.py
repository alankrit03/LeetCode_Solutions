# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(ListNode):
    def __init__(self):
        pass
    def create_list(self , arr):
        n = len(arr)

        head = ListNode(arr[0])
        ptr=head

        for i in range(1,n):
            ptr.next = ListNode(arr[i])
            ptr = ptr.next


        return head

    def print_list(self,head):
        ptr = head
        while ptr.next:
            print(ptr.val , end=' -> ')
            ptr = ptr.next

        print(ptr.val)

list1=LinkedList()
array = [11,22,33,44,55,66,77,88]
head = list1.create_list(array)
list1.print_list(head)