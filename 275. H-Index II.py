class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi) // 2

            if citations[mid] < n - mid:
                lo = mid + 1
            else:
                hi = mid

        return n - lo