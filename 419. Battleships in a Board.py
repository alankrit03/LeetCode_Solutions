class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        if not row:
            return 0
        col = len(board[0])
        if not col:
            return 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def DFS(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] == '.':
                return

            board[i][j] = '.'
            for d in range(4):
                DFS(i + dr[d], j + dc[d])

        ans = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    ans += 1
                    DFS(i, j)
                    # print(ans)
                    # print(board)

        return ans