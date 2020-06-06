class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        n = len(s)
        if not s:
            return 0
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                break
        else:
            return n - i

        return n - i - 1