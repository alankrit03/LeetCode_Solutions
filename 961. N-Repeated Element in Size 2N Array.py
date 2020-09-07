class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        cache = set()
        for x in A:
            if x in cache:
                return x
            cache.add(x)