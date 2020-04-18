"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head

        def get_last_node(ptr):
            while ptr.next:
                ptr = ptr.next
            return ptr

        while node:
            if node.child:
                ptr = node.next
                node.next = node.child
                node.next.prev = node
                temp = get_last_node(node.child)
                node.child = None
                temp.next = ptr
                if ptr:
                    ptr.prev = temp
            node = node.next

        return head