class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def ispossible(limit):
            count = 0
            curr = 0
            for x in weights:
                if x > limit:
                    return False
                if curr + x > limit:
                    count += 1
                    curr = x
                else:
                    curr += x
            count += 1
            if count <= D:
                return True
            return False

        l, h = -1, sum(weights)

        while h - l > 1:
            m = (h + l) // 2

            if ispossible(m):
                h = m
            else:
                l = m
        return h