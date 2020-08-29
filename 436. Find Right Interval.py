class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def sortFn(x):
            return x[1][0]

        def getPos(lo, target):
            hi = n - 1

            while lo < hi:
                mid = (lo + hi) // 2

                if intervals[mid][1][0] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            if intervals[hi][1][0] >= target:
                return intervals[hi][0]
            return -1

        n = len(intervals)
        intervals = list(enumerate(intervals))
        intervals.sort(key=sortFn)

        # print(intervals)

        ans = [-1] * n

        for i in range(n):
            ans[intervals[i][0]] = getPos(i + 1, intervals[i][1][1])
        return ans