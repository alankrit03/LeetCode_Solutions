class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        def last(x):
            return x[1], x[0]

        events.sort(key=last)
        # print(events)
        curr_day = events[0][0]
        res = set()

        for start, end in events:
            for i in range(start, end + 1):
                if i not in res:
                    res.add(i)
                    break

        return len(res)