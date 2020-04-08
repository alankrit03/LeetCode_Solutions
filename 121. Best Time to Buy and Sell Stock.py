class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        if not arr:return 0
        max_ = arr[-1]
        ans = 0

        for i in range(len(arr)-2, -1, -1):
            ans = max(max_ - arr[i], ans)
            max_ = max(max_ , arr[i])

        return ans