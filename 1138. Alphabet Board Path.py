class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        self.ans = []
        n = len(target)
        self.found = 0

        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        row = 5
        col = 5

        dr = [0, -1, 0, 1]
        dc = [-1, 0, 1, 0]
        name = ['L', 'U', 'R', 'D']

        def isvalidpos(i, j):
            if (i < 0 or j < 0) or (j > 4 or i > 5):
                return False
            if i == 5 and j != 0:
                return False
            return True

        def recur(idx, i, j, path):
            if idx == n:
                print(path)
                self.ans = path[:]
                self.found = 1
                return

            if not isvalidpos(i, j):
                return

            while idx < n and target[idx] == board[i][j]:
                print(path)
                idx += 1
                path.append('!')

            for x in range(4):

                path.append(name[x])
                recur(idx, i + dr[x], j + dc[x], path)
                path.pop()

                if self.found:
                    return

        recur(0, 0, 0, [])
        return "".join(self.ans)


ob = Solution()
print(ob.alphabetBoardPath('leet'))