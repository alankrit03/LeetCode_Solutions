class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cache = {'L': (-1, 0),
                 'U': (0, 1),
                 'R': (1, 0),
                 'D': (0, -1)
                 }

        x = y = 0
        for move in moves:
            x += cache[move][0]
            y += cache[move][1]

        if x == 0 and y == 0:
            return True
        return False