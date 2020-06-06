class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = nums[0]
        second_max = 0

        for i in range(1, len(nums)):
            if nums[i] >= max_val:
                second_max = max_val
                max_val = nums[i]
            elif nums[i] > second_max:
                second_max = nums[i]

        return (max_val - 1) * (second_max - 1)