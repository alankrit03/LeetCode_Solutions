class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        cache = set(s[0])
        i = 0
        j = ans = curr = 1

        while i <= j and j < len(s):
            # print(cache)
            # print(f'i={i} j={j}\n')
            if s[j] in cache:
                ans = max(ans, curr)
                while s[j] in cache:
                    cache.remove(s[i])
                    i += 1
                    curr -= 1
            cache.add(s[j])
            curr += 1
            j += 1

        return max(ans, curr)