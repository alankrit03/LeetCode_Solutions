class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def ispossible(limit):
            count = 1
            curr = 0
            for x in nums:
                if curr + x > limit:
                    count += 1
                    curr = x
                else:
                    curr += x
            if count <= m:
                return True
            return False

        l, h = max(nums), sum(nums)

        while l < h:
            mid = (l + h) // 2

            if ispossible(mid):
                h = mid
            else:
                l = mid + 1
        return l
