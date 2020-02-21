class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        h = len(nums) - 1
        result = [-1, -1]
        while (l <= h):
            m = (l + h) // 2

            if nums[m] == target:
                result[0] = m
                h = m - 1

            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1

        l = 0
        h = len(nums) - 1

        while (l <= h):
            m = (l + h) // 2

            if nums[m] == target:
                result[1] = m
                l = m + 1

            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1

        return result