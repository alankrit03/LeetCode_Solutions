class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if not n % i:
                k -= 1
            if not k:
                return i

        return -1