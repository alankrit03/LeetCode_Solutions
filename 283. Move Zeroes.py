class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeroes = nums.count(0)
        if not num_zeroes:
            return
        i, n = 0, len(nums)
        while i < n-num_zeroes:
            if nums[i]:
                i += 1
            else:
                nums.append(nums.pop(i))

print(Solution.moveZeroes(Solution, [0,1,0,23,4]))