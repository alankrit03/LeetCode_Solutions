class Solution:
    def lengthOfLIS(self, nums: List[int]):
        if not nums:
            return 0

        def getPos(x):
            l, h = 0, ans
            while l < h:
                m = (l + h) // 2

                if dp[m] < x:
                    l = m + 1
                else:
                    h = m
            return l

        n = len(nums)
        dp = [nums[0]]
        ans = 1
        for i in range(1, n):
            pos = getPos(nums[i])
            if pos == ans:
                dp.append(nums[i])
                ans += 1
            else:
                dp[pos] = nums[i]

        return ans