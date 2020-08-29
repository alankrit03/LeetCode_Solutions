class Solution():
    def canJump(self, nums):
        curr = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= curr:
                curr = i

        print(Index.Mon)

        return not bool(curr)


import enum
class Index(enum.Enum):
    Sun:1
    Mon=2

print(Solution().canJump([1,2,3,4,5,6]))