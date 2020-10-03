from heapq import heappush, heappop


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def sortFn(x):
            return x[1]

        trips.sort(key=sortFn)

        curr = 0
        heap = []

        for trip in trips:
            while heap and heap[0][0] <= trip[1]:
                _, p = heappop(heap)
                curr -= p

            if curr + trip[0] <= capacity:
                heappush(heap, (trip[2], trip[0]))
                curr += trip[0]
            else:
                return False

        return True
