from heapq import heapify, heappop
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_heap = [-x for x in piles]
        heapify(piles)
        heapify(max_heap)

        n = len(piles)
        i = 0
        ans = 0
        while i < n:
            heappop(max_heap)
            ans += -(heappop(max_heap))
            heappop(piles)
            i += 3
        # print(max_heap)
        return ans


"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
APPROACH 2
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=1)
        n = 2*len(piles)//3
        i=1
        ans = 0
        while i<n:
            ans += piles[i]
            i+=2
        # print(max_heap)
        return ans