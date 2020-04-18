class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return -1

        current_max = current_min = ans = nums[0]

        for i in range(1, len(nums)):
            temp = current_max

            current_max = max(current_max * nums[i], current_min * nums[i], nums[i])

            current_min = min(temp * nums[i], current_min * nums[i], nums[i])

            ans = max(ans, current_max)

        return ans