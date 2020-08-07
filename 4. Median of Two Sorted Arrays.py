import heapq


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        k = ((n1 + n2) // 2) + 1

        i = 0
        while i < n2:
            heapq.heappush(nums1, nums2[i])
            i += 1

        s = n1 + n2
        while s > k:
            heapq.heappop(nums1)
            s -= 1

        if (n1 + n2) % 2 == 1:
            return heapq.heappop(nums1)
        else:
            return (heapq.heappop(nums1) + heapq.heappop(nums1)) / 2