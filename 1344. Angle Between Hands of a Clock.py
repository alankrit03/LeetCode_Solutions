class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_1 = minutes * 6

        hour %= 12
        angle_2 = hour * 30 + (minutes / 60) * 30
        ans = abs(angle_2 - angle_1)
        return min(ans, 360 - ans)