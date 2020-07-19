class RecentCounter:

    def __init__(self):
        self.time = []
        self.n = 0

    def ping(self, t: int) -> int:
        self.time.append(t)
        self.n += 1
        return self._getRequests(t - 3000)

    def _getRequests(self, t):
        l, h = -1, self.n - 1

        while h - l > 1:
            m = (l + h) // 2

            if self.time[m] < t:
                l = m
            else:
                h = m
        return self.n - h

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)