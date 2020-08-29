class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def ispossible(mid):
            total = 0
            for x in nums:
                total += math.ceil(x / mid)

            if total <= threshold:
                return True
            return False

        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2

            if ispossible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo