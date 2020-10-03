class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]

        grid = [[0] * 8 for i in range(8)]
        for queen in queens:
            grid[queen[0]][queen[1]] = 1

        ans = []

        def bfs(i, j, d):
            if i < 0 or j < 0 or i >= 8 or j >= 8:
                return

            if grid[i][j]:
                ans.append([i, j])
                return

            bfs(i + dr[d], j + dc[d], d)

        for i in range(8):
            bfs(*king, i)

        return ans