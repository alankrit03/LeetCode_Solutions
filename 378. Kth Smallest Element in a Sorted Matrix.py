import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [0] * n
        for i in range(n):
            heap[i] = (matrix[i][0], i, 0)

        sorted_arr = []

        while k:
            val, row, col = heapq.heappop(heap)
            sorted_arr.append(val)
            if col < n - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            k -= 1
        return sorted_arr[-1]