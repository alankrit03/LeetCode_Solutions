# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n + 1

        while h - l > 1:
            m = (h + l) // 2

            if guess(m) > -1:
                l = m
            else:
                h = m
        return l