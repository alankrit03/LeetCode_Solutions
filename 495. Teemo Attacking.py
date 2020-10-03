class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        n = len(timeSeries)
        ans = 0
        start = timeSeries[0]
        currEnd = start + duration

        for i in range(1, n):
            x = timeSeries[i]

            if currEnd < x:
                ans += currEnd - start
                start = x
            currEnd = x + duration
        else:
            ans += currEnd - start

        return ans