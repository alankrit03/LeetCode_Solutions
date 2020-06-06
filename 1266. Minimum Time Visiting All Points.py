class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for i in range(1, len(points)):
            curr = points[i]
            prev = points[i - 1]

            time += max(max(curr[0], prev[0]) - min(curr[0], prev[0]),
                        max(curr[1], prev[1]) - min(curr[1], prev[1])
                        )
        return time