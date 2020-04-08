class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_, second_ = 0, -10_000_000

        for i in range(1, len(nums)):
            if nums[i] >= nums[max_]:
                second_ = nums[max_]
                max_ = i
            elif nums[i] >= second_:
                second_ = nums[i]

        if nums[max_] >= 2 * second_:
            return max_
        return -1