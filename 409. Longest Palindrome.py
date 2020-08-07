class Solution:
    def longestPalindrome(self, s: str) -> int:
        cache = {}

        for x in s:
            try:
                cache[x] += 1
            except:
                cache[x] = 1

        odd = False
        long = 0

        for key, val in cache.items():
            if val % 2 == 0:
                long += val
            else:
                long += val - 1
                odd = True
        if odd:
            return long + 1
        return long