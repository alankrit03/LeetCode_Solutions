class Solution:
    def minEatingSpeed(self, nums: List[int], H: int) -> int:
        def ispossible(n):
            count = 0
            for x in nums:
                if x%n :
                    count += 1
                count += x//n
            if count <= H:
                return True
            return False

        l, h = 1, sum(nums)

        while l < h:
            mid = (l + h) // 2

            if ispossible(mid):
                h = mid
            else:
                l = mid + 1
        return l