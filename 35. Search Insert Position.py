class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        l, h = -1, len(nums)

        while h - l > 1:
            m = (l + h) // 2

            if nums[m] < target:
                l = m
            else:
                h = m
        return h