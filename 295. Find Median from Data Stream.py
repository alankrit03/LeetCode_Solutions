import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []  # Larger Half of heap
        self.min = 0
        self.maxheap = []  # Containing smaller half of stream
        self.max = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        if self.min == self.max:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            self.max += 1
        else:
            self.min += 1

        # print(self.maxheap)
        # print(self.minheap)

        # print()

    def findMedian(self) -> float:
        if self.max == self.min:
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return -self.maxheap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()