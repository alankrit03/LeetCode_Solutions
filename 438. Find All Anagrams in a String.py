class Solution:
    from collections import Counter
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:
            return
        len_p = len(p)
        c = Counter(p)
        window = Counter(s[:len_p - 1])
        ans = []
        for i in range(0, len(s) - len_p + 1):
            window[s[i + len_p - 1]] += 1
            # print(window)
            if window == c:
                ans.append(i)
            window -= (Counter(s[i:i + 1]))

        return ans
