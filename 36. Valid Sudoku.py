class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sq_cache = {}
        col_cache = {}
        """The below for loop initialises the cache to be used easily later on."""

        for i in range(3):
            for j in range(3):
                sq_cache[(i, j)] = set()

        for i in range(9):
            col_cache[i] = set()

        """main loop"""
        for i in range(9):
            row_set = set()

            for j in range(9):
                element = board[i][j]
                if element != '.':

                    if element in row_set:
                        return False
                    else:
                        row_set.add(element)

                    if element in col_cache[j]:
                        return False
                    else:
                        col_cache[j].add(element)

                    if element in sq_cache[(i // 3, j // 3)]:
                        return False
                    else:
                        sq_cache[(i // 3, j // 3)].add(element)

        return True