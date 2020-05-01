class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False

        mask = 1
        while mask < num:
            mask *= 4

        return not num % mask