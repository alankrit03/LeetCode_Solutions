class Solution:
    def trailingZeroes(self, n: int) -> int:
        power = 5
        ans = 0

        while power <= n:
            ans += n // power

            power *= 5

        return ans