class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isPossible(x):
            count = m - 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= x:
                    count -= 1
                    curr = position[i]
                if not count:
                    return True
            return False

        n = len(position)
        position.sort()
        lo = 1
        hi = position[-1] - position[0] + 1

        while hi - lo > 1:
            mid = lo + (hi - lo) // 2

            if isPossible(mid):
                lo = mid
            else:
                hi = mid

        return lo