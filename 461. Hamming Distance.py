class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def int_to_bin(n):
            s = ''
            while n:
                s += str(n % 2)
                n //= 2

            s += '0' * (32 - len(s))
            return s

        x = int_to_bin(x)
        y = int_to_bin(y)

        ans = 0
        for i in range(32):
            if x[i] != y[i]:
                ans += 1

        return ans