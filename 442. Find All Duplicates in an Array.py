class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        ans = []
        for x in nums:
            x = abs(x) - 1

            if nums[x] < 0:
                ans.append(x + 1)
            else:
                nums[x] = -nums[x]

        return ans