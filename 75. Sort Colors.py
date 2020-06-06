class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        n = len(nums)

        i, j = 0, 1

        while n > j > i and i < n:
            if nums[i] <= nums[j]:
                j += 1
                continue
            if nums[i] == 0:
                i += 1

            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

        j -= 1

        while j > i:
            if nums[j] == 2:
                j -= 1
                continue

            if nums[i] <= nums[j]:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]

arr = [0,0,1,2,1]
Solution().sortColors(arr)
print(arr)
