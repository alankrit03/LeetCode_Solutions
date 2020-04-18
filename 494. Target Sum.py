class Solution:
    def __init__(self):
        self.cache = {}

    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        n = len(nums)

        def recur(total, i):
            if i == n:
                if not total:
                    return 1
                return 0

            if (total, i) in self.cache:
                return self.cache[(total, i)]

            x = recur(total - nums[i], i + 1)
            y = recur(total + nums[i], i + 1)

            self.cache[(total, i)] = x + y

            return x + y

        ans = recur(S, 0)

        return ans