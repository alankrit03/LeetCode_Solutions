class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        dx = 0
        dy = 1
        for d in 4 * instructions:
            if d == 'L':
                dx, dy = -dy, dx
            elif d == 'R':
                dx, dy = dy, -dx
            else:
                x += dx
                y += dy

        return (x, y) == (0, 0)