class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = [0] * n
        col = [0] * m

        for point in indices:
            row[point[0]] += 1
            col[point[1]] += 1

        odd_val = 0

        for i in range(n):
            for j in range(m):
                if (row[i] + col[j]) % 2:
                    odd_val += 1

        return odd_val