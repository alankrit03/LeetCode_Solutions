class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i]:
                curr += 1
            else:
                ans = max(ans,curr)
                curr = 0
        return max(ans,curr)