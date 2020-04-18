class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cache = set()
        for x in arr:
            if x * 2 in cache:
                return True
            if x % 2 == 0 and x // 2 in cache:
                return True

            cache.add(x)
        else:
            return False