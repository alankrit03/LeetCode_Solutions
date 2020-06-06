class Solution:
    def canBeEqual(self, target, arr) -> bool:
        from collections import Counter

        return Counter(target) == Counter(arr)