from heapq import heapify, heappush, heappop


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        heap = []
        row = len(mat)
        col = len(mat[0])

        for j in range(col):
            for temp in range(2):
                j_ = j
                i = 0
                while j_ < col and i < row:
                    if not temp:
                        heappush(heap, mat[i][j_])
                    else:
                        mat[i][j_] = heappop(heap)
                    i += 1
                    j_ += 1

        for i_ in range(1, row):
            for temp in range(2):
                i = i_
                j = 0
                while j < col and i < row:
                    if not temp:
                        heappush(heap, mat[i][j])
                    else:
                        mat[i][j] = heappop(heap)
                    i += 1
                    j += 1

        return mat