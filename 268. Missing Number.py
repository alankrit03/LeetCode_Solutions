class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for x in nums:
            total += x

        return ((n * (n + 1)) // 2) - total