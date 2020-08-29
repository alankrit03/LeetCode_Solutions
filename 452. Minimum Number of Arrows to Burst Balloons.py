class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort(key=lambda x: x[0])
        if not points:
            return 0
        prev = float('inf')
        arrow = 1
        for b, e in points:
            if prev >= b:
                prev = min(prev, e)
            else:
                arrow += 1
                prev = e
        return arrow

