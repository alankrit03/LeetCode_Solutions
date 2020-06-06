class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        def right(row, j):
            for i in range(j + 1, 8):
                if board[row][i] == 'B':
                    return 0
                if board[row][i] == 'p':
                    # print('right',row,j)
                    return 1
            return 0

        def left(row, j):
            for i in range(j - 1, -1, -1):
                if board[row][i] == 'B':
                    return 0
                if board[row][i] == 'p':
                    return 1
            return 0

        def up(i, col):
            for idx in range(i - 1, -1, -1):
                if board[idx][col] == 'B':
                    return 0
                if board[idx][col] == 'p':
                    # print(,idx,col)
                    return 1
            return 0

        def down(i, col):
            for idx in range(i + 1, 8):
                if board[idx][col] == 'B':
                    return 0
                if board[idx][col] == 'p':
                    # print(idx,col)
                    return 1
            return 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    pos = [i, j]
                    break

        # print(pos)
        return right(*pos) + left(*pos) + up(*pos) + down(*pos)