class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, h = 0, len(nums)

        while h - l > 1:
            m = (l + h) // 2

            if nums[m] > nums[m - 1]:
                l = m
            else:
                h = m
        return l