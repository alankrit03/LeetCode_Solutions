class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        cache = []
        from collections import Counter
        for x in strs:
            temp = Counter(x)
            if temp in cache:
                ans[cache.index(temp)].append(x)
            else:
                cache.append(temp)
                ans.append([x])

        return ans