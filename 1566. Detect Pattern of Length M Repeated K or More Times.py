class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        n = len(arr)

        def isPatternPresent(idx):
            for i in range(m):
                counter = 0
                j = idx
                ele = arr[j]
                while j < n:
                    if arr[j] != ele:
                        return False
                    j += m
                    counter += 1
                    if counter>=k:
                        break

                if counter >= k:
                    idx += 1
                else:
                    return False
            return True

        for i in range(n):
            if isPatternPresent(i):
                return True

        return False

ob = Solution()
arr = [1,2,4,4,4,4]
print(ob.containsPattern(arr,1,3))