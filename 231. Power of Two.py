class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        return not (2 ** 32) % n
