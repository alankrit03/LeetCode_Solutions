class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        n = len(arr2)
        for x in arr1:
            i = 0
            while i < n:
                if not abs(x - arr2[i]) > d:
                    break
                i += 1
            else:
                ans += 1

        return ans