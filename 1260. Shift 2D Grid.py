class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r = len(grid)
        col = len(grid[0])
        k %= r * col
        temp = []

        for row in grid:
            temp.extend(row)

        temp = temp[-k:] + temp[:-k]
        grid = []
        for i in range(0, len(temp), col):
            grid.append(temp[i:i + col])

        return grid