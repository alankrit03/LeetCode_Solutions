class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, h = 0, len(A)
        while h - l > 1:
            m = (l + h) // 2

            if A[m] > A[m - 1]:
                l = m
            else:
                h = m
        return l