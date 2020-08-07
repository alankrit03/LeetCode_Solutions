class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return ''

        def expand(i, j):
            if i > j:
                return

            while (i >= 0 and j < n and s[i] == s[j]):
                self.count += 1
                i -= 1
                j += 1

        n = len(s)
        self.count = 0

        for idx in range(n):
            expand(idx, idx)
            expand(idx, idx + 1)

        return self.count