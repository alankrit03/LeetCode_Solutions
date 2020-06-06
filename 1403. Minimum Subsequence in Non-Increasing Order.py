class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        n = len(nums)
        left = 0
        total = sum(nums)
        for i in range(0, n):
            left += nums[i]
            if left > (total - left):
                return nums[:i + 1]

