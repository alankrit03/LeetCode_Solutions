class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                temp = stones[-1] - stones[-2]
                stones.pop()
                stones[-1] = temp

        if stones:
            return stones[-1]
        return 0