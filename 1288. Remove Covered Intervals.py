class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        def sortFn(x):
            return (x[0], -x[1])

        intervals.sort(key=sortFn)

        end = intervals[0][1]
        ans = 1
        for i in range(1, len(intervals)):
            x = intervals[i]
            if end < x[1]:
                ans += 1
                end = x[1]

        return ans