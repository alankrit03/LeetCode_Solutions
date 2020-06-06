class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_present(i, j, idx):
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == '' or board[i][j] != word[idx]:
                return False

            if board[i][j] == word[idx] and idx == n - 1:
                return True
            temp = board[i][j]
            board[i][j] = ''
            result = (is_present(i - 1, j, idx + 1) or is_present(i + 1, j, idx + 1) or is_present(i, j - 1,
                                                                                                   idx + 1) or is_present(
                i, j + 1, idx + 1))

            board[i][j] = temp
            return result

        row = len(board)
        col = len(board[0])
        n = len(word)
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if is_present(i, j, 0):
                        return True
        return False