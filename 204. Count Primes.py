class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        arr = [True] * (n)
        arr[0] = arr[1] = False

        for i in range(2, int(sqrt(n)) + 1):
            if arr[i]:
                for j in range(2 * i, n, i):
                    arr[j] = False

        ans = 0

        for x in arr:
            if x:
                ans += 1

        return ans