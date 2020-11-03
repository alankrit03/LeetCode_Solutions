class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def isTrue(x):
            count = 0
            for y in nums:
                if y >= x:
                    count += 1

            return count

        if not nums:
            return 0
        lo = 0
        hi = len(nums) + 1

        while hi - lo > 1:
            mid = (lo + hi) // 2
            count = isTrue(mid)
            if count >= mid:
                lo = mid
            else:
                hi = mid
            print(lo, hi)
        if isTrue(lo) == lo:
            return lo
        return -1