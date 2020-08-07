class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check_neighbor(x, y):
            if x < 0 or y < 0 or x >= n or y >= m:
                return 0
            if board[x][y] == -1 or board[x][y] == 1:
                return 1
            return 0

        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                c = 0
                for curr in range(8):
                    c += check_neighbor(i + dr[curr], j + dc[curr])

                if board[i][j]:
                    if c < 2 or c > 3:
                        board[i][j] = -1
                else:
                    if c == 3:
                        board[i][j] = 2

        for i in range(n):
            for j in range(m):
                if board[i][j] <= 0:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
