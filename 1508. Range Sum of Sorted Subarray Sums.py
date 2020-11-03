from heapq import heapify, heappop


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []

        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += nums[j]
                heap.append(sum_)

        # print(heap)
        heapify(heap)
        # print(heap)
        for i in range(left - 1):
            heappop(heap)
        ans = 0
        for i in range(left, right + 1):
            ans += heappop(heap)
        return ans % 1000000007