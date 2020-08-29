class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or (not matrix[0]):
            return False

        row = len(matrix)
        col = len(matrix[0])

        n = row * col

        def get_pos(x):
            if x % col:
                return (x // col, (x % col) - 1)
            return ((x // col) - 1, col - 1)

        # print(get_pos(1))

        lo, hi = 1, n
        while lo < hi:
            mid = (hi + lo) // 2
            i, j = get_pos(mid)

            if matrix[i][j] >= target:
                hi = mid
            else:
                lo = mid + 1

        i, j = get_pos(hi)
        if matrix[i][j] == target:
            return True
        return False