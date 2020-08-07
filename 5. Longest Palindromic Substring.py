class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        def expand(i, j):
            if i > j:
                return

            while (i >= 0 and j < n and s[i] == s[j]):
                curr = j - i + 1

                if curr > self.max:
                    self.max = curr
                    self.ans = s[i:j + 1]

                i -= 1
                j += 1

        n = len(s)
        self.ans = ''
        self.max = 0

        for idx in range(n):
            expand(idx, idx)
            expand(idx, idx + 1)

        return self.ans