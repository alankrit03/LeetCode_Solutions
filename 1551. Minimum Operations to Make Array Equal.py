class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for i in range(n // 2):
            x = 2 * i + 1
            ans += n - x

        return ans
