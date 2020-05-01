class Solution:
    from collections import Counter
    def firstUniqChar(self, s: str) -> int:
        cache = Counter(s)

        for i in range(len(s)):
            if cache[s[i]] == 1:
                return i
        else:
            return -1