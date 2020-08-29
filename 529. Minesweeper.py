class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row = len(board)
        col = len(board[0])

        # if board[click[0]][click[1]]=='M':
        # board[click[0]][click[1]]='X'
        # return board

        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]

        def check_mines(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return 0
            if board[i][j] == 'M':
                return 1
            return 0

        def bfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] == 'B':
                return

            if board[i][j] == 'M':
                board[i][j] = 'X'
                return

            mine = 0
            for d in range(8):
                mine += check_mines(i + dr[d], j + dc[d])

            if mine:
                board[i][j] = str(mine)
                return

            board[i][j] = 'B'
            for d in range(8):
                bfs(i + dr[d], j + dc[d])

            return

        bfs(*click)
        return board
