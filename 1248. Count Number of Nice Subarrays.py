class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def findNext(idx):
            for i in range(idx, n):
                if nums[i] % 2:
                    return i
            return n

        def findPrev(idx):
            for i in range(idx, -1, -1):
                if nums[i] % 2:
                    return i

            return -1

        i = 0
        nextOdd = {}
        while i < n:
            if nums[i] % 2:
                pos = findNext(i + 1)
                nextOdd[i] = pos - i
                i = pos
            else:
                i += 1

        prevOdd = {}
        i = n - 1
        while i >= 0:
            if nums[i] % 2:
                pos = findPrev(i - 1)
                prevOdd[i] = i - pos
                i = pos
            else:
                i -= 1

        ans = 0
        cache = {}
        count = 0
        for i in range(n):
            if nums[i] % 2:
                count += 1
                cache[count] = i
                if count >= k:
                    t = count - k + 1
                    ans += prevOdd[cache[t]] * nextOdd[i]

        return ans


