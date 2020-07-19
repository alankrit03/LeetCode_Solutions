from collections import deque


class KthLargest:

    def __init__(self, k, num):
        self.k = k
        self.arr = deque()
        self.n = 0
        for x in num:
            self.add(x)

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.n += 1

        self.ladder(self.n - 1)

        if self.n > self.k:
            self.arr[0], self.arr[self.n - 1] = self.arr[self.n - 1], self.arr[0]
            self.arr.pop()
            self.n -= 1
            self.min_heapify(0)

        return self.arr[0]

    def ladder(self, i):
        while i > 0 and self.arr[(i - 1) // 2] > self.arr[i]:
            self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
            i = (i - 1) // 2

    def min_heapify(self, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < self.n and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < self.n and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)


# Your KthLargest object will be instantiated and called as such:
nums = [4, 5, 8, 2]
kthLargest = KthLargest(3, nums)

print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
