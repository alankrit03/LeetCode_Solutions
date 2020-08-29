class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def isvalid(x, y):
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == 0 or grid[x][y] == 2:
                return False
            return True

        row = len(grid)
        col = len(grid[0])

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        queue = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        ans = 0

        while queue:
            x, y, level = queue.popleft()

            for drn in range(4):
                x1 = x + dr[drn]
                y1 = y + dc[drn]
                if isvalid(x1, y1):
                    grid[x1][y1] = 2
                    queue.append((x1, y1, level + 1))
                    ans = max(ans, level + 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return ans