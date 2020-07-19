class MyCalendar:

    def __init__(self):
        self._time = []
        self._n = 0

    def _getPos(self, t):
        l, h = -1, self._n

        while h - l > 1:
            m = (l + h) // 2

            if self._time[m][0] < t:
                l = m
            else:
                h = m
        return h

    def book(self, start: int, end: int) -> bool:
        if not self._n:
            self._time.append((start, end))
            self._n += 1
            return True

        pos = self._getPos(start)
        # print(self._time,pos)
        # print(start,end)
        if pos == self._n:
            if start < self._time[pos - 1][1]:
                return False
            self._time.append((start, end))
            self._n += 1
            return True
        else:
            if end > self._time[pos][0]:
                return False
            if pos and start < self._time[pos - 1][1]:
                return False
            self._time.insert(pos, (start, end))
            self._n += 1
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)