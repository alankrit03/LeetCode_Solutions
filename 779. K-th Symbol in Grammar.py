class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def element(n, k, num):
            if n == 1:
                return 0

            if k > num:
                return ((element(n - 1, k - num, num // 2)) + 1) % 2
            else:
                return element(n - 1, k, num // 2)

        ele = element(N, K, 2 ** (N - 2))
        return ele