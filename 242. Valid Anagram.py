class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)

        if Counter(t) == s:
            return True
        else:
            return False