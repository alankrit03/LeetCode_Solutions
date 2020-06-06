from collections import Counter


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))

        for i in range(len(words)):
            words[i] = f(words[i])

        ans = [0] * len(queries)

        for i in range(len(queries)):
            n = f(queries[i])
            temp = 0
            for word in words:
                if word > n:
                    temp += 1
            ans[i] = temp

        return ans