class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def ispossible(x):
            total = 0
            for i in range(1, m + 1):
                total += min(x // i, n)
            if total >= k:
                return True
            return False

        l, h = 1, m * n

        while l < h:
            mid = (l + h) // 2
            if ispossible(mid):
                h = mid
            else:
                l = mid + 1
        return l
