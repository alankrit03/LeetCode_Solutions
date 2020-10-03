class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        max_ = 0
        n = len(times)
        self.timeline = []
        cache = {}

        for i in range(n):
            p = persons[i]
            if p not in cache:
                cache[p] = 0
            cache[p] += 1
            if max_ <= cache[p]:
                self.timeline.append((p, times[i]))
                max_ = cache[p]

        # print(self.timeline)

    def q(self, t: int) -> int:
        lo, hi = 0, len(self.timeline)

        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.timeline[mid][1] > t:
                hi = mid
            else:
                lo = mid

        return self.timeline[lo][0]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)