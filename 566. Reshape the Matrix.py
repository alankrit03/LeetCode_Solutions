class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        if len(nums) * len(nums[0]) != r * c:
            return nums

        for row in nums:
            temp.extend(row)

        nums = []

        for i in range(0, len(temp), c):
            nums.append(temp[i:i + c])

        return nums