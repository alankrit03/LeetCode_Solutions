class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        mask = 1
        power = 0

        while mask <= n:
            if mask ^ n == n - mask:
                ans += 2 ** (31 - power)

            mask <<= 1
            power += 1

        return ans