class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        m, n = len(matrix), len(matrix[0])

        def next_move_invalid(i, j):
            i += directions[curr_dir][0]
            j += directions[curr_dir][1]

            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] == 'n':
                return True

            return False

        ans = []

        x = 0
        y = -1
        flag = 0
        while True:

            if next_move_invalid(x, y):
                if flag:
                    break
                flag += 1
                curr_dir = (curr_dir + 1) % 4
                continue

            flag = 0
            x += directions[curr_dir][0]
            y += directions[curr_dir][1]
            ans.append(matrix[x][y])
            matrix[x][y] = 'n'

        return ans