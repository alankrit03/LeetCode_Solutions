class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if not envelopes:
            return 0

        def sortFn(x):
            return (x[0], -x[1])

        envelopes.sort(key=sortFn)

        def isBigger(e1, e2):
            return e2 > e1

        def getPos(x):
            lo, hi = 0,ans

            while lo < hi:
                mid = (lo + hi) // 2

                if dp[mid]< x:
                    lo = mid+1
                else:
                    hi = mid
            return lo

        n = len(envelopes)
        dp = [envelopes[0][1]]
        ans = 1
        print(envelopes)
        print(dp)
        for i in range(1, n):
            pos = getPos(envelopes[i][1])
            if pos == ans:
                dp.append(envelopes[i][1])
                ans += 1
            else:
                dp[pos] = envelopes[i][1]
            # print(dp)
        return ans

ob = Solution()
arr = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
print(ob.maxEnvelopes(arr))