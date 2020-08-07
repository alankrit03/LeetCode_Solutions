class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.cache = {}

        def recur(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if (i, j) in self.cache:
                return self.cache[(i, j)]

            if s[i] == s[j]:
                ans = recur(i + 1, j - 1) + 2
            else:
                ans = max(recur(i + 1, j), recur(i, j - 1))

            self.cache[(i, j)] = ans
            return ans

        return recur(0, len(s) - 1)
