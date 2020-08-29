

class Solution:
    def print_board(self):
        for i in range(9):
            print(*board[i])

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.flag = False

        def is_valid(i, j, ele):
            for a in range(9):
                if board[i][a] == ele or board[a][j] == ele:
                    return False
            i = (i // 3) * 3
            j = (j // 3) * 3
            for a in range(i, i + 3):
                for b in range(j, j + 3):
                    if board[a][b] == ele:
                        return False

            return True

        def find_empty(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return (i, j)

        temp = find_empty(board)

        if not temp:
            self.flag = True
            return 0
        else:
            x, y = temp

        for num in range(1, 10):
            if is_valid(x, y, str(num)):
                board[x][y] = str(num)
                self.solveSudoku(board)
                if not self.flag:
                    board[x][y] = '.'
                else:
                    break
        return board


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".",".",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

ob = Solution()


ob.print_board(ob.solveSudoku(board))