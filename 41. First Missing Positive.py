class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == []:
            return 1
        cache = {}

        for x in nums:
            if x > 0:
                cache[x] = 1
        n = len(nums)
        for i in range(1, n + 1):
            if not cache.get(i):
                return i

        return n + 1


"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
APPROACH 2:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            x = nums[i]
            while 0 < x <= n:
                if nums[i] == nums[x - 1]:
                    break
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
                x = nums[i]
                if x == i + 1:
                    break
        # print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1