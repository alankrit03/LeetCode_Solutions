class Solution:
    def rob(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) < 3:
            return max(arr)

        def rob1(nums):
            if not nums:
                return 0
            ans = [nums[0]]
            n = len(nums)
            if n > 1:
                ans.append(max(nums[1], nums[0]))
            for i in range(2, n):
                x = nums[i] + ans[i - 2]
                ans.append(max(x, ans[-1]))

            return ans[-1]

        return max(rob1(arr[1:]), rob1(arr[:-1]))