class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def ispossible(wait):
            bouq = 0
            i = 0
            j = -1

            while j < n - 1:
                if bloomDay[j + 1] > wait:
                    i = j+2
                    j += 1
                else:
                    j+=1
                if j - i + 1 == k and j<n:
                    print(bloomDay[i:j+1])
                    bouq += 1
                    i = j+1
            if bouq >= m:
                return True
            else:
                False

        l, h = 1, max(bloomDay)

        while l < h:
            mid = l + (h - l) // 2

            if ispossible(mid):
                h = mid
            else:
                l = mid + 1

        return l


ob = Solution()
print(ob.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))