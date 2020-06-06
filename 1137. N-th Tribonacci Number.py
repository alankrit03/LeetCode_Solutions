class Solution:
    def tribonacci(self, n: int) -> int:
        f = 0
        s = t = 1
        if n == 0:
            return 0
        elif n < 3:
            return 1

        for i in range(n - 2):
            fo = f + s + t
            f = s
            s = t
            t = fo
        return fo