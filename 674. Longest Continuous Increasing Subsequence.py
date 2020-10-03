class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        curr = 1

        for i in range(len(nums)):
            if not i:
                ans = 1
            else:
                if nums[i] > nums[i - 1]:
                    curr += 1
                else:
                    curr = 1

                ans = max(ans, curr)

        return ans
