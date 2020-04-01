class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not len(nums):
            return -1

        pivot = self.get_pivot(nums)
        # print(pivot)
        if target >= nums[0]:
            return self.binary_search(nums, target, 0, pivot)
        else:
            return self.binary_search(nums, target, pivot + 1, len(nums) - 1)

    def get_pivot(self, arr):
        l, h = 0, len(arr)
        n = h - 1
        while h - l > 1:
            m = (l + h) // 2

            if arr[m] >= arr[0]:
                l = m
            else:
                h = m

        return l

    def binary_search(self, nums, target, l, h) -> int:

        # print(l, h)
        while h >= l:
            m = (h + l) // 2

            if target > nums[m]:
                l = m + 1
            elif target == nums[m]:
                return m
            else:
                h = m - 1

        return -1