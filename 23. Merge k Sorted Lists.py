# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if not n:
            return
        heap = []
        cache = {}
        i = 0
        for node in lists:
            if node:
                heap.append((node.val, i))
                cache[i] = lists[i]
            i += 1
        if not heap:
            return
        print(heap)
        heapq.heapify(heap)
        temp = heapq.heappop(heap)
        head = ListNode(temp[0])
        ptr = head

        temp2 = cache[temp[1]]
        if temp2.next:
            heapq.heappush(heap, (temp2.next.val, temp[1]))
            cache[temp[1]] = temp2.next

        while heap:
            temp = heapq.heappop(heap)
            ptr.next = ListNode(temp[0])
            ptr = ptr.next

            node = cache[temp[1]]
            if node.next:
                heapq.heappush(heap, (node.next.val, temp[1]))
                cache[temp[1]] = node.next

        return head