class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == []:
            return 1
        cache = {}

        for x in nums:
            if x > 0:
                cache[x] = 1
        n = len(nums)
        for i in range(1, n + 1):
            if not cache.get(i):
                return i

        return n + 1