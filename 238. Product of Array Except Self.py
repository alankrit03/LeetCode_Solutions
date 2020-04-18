class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[n - 1] = 1
        for i in range(n - 2, -1, -1):
            ans[i] = ans[i + 1] * nums[i + 1]

        left = 1

        for i in range(n):
            ans[i] = left * ans[i]
            left = left * nums[i]

        return ans