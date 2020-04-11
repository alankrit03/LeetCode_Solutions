class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        needle_n = len(needle)

        for i in range(len(haystack) - needle_n + 1):
            if haystack[i:i + needle_n] == needle:
                return i
        return -1