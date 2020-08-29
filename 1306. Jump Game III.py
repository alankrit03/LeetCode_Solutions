class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.cache = set()
        n = len(arr)
        queue = collections.deque()
        queue.append(start)

        while queue:
            pos = queue.popleft()
            if arr[pos] == 0:
                return True
            if pos not in self.cache:
                self.cache.add(pos)

                if pos - arr[pos] >= 0:
                    queue.append(pos - arr[pos])
                if pos + arr[pos] < n:
                    queue.append(pos + arr[pos])
        return False