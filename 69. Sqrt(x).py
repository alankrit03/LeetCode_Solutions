class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x + 1
        while (h - l > 1):
            m = (l + h) // 2

            if m * m <= x:
                l = m
            else:
                h = m
        return l
