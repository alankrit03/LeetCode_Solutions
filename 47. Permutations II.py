class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        n = len(nums)
        self.seen = [False] * n

        def recur(curr, size):
            if size == n:
                self.ans.append(curr[:])
                return

            cache = set()
            for i in range(n):
                if not self.seen[i] and (nums[i] not in cache):
                    cache.add(nums[i])
                    self.seen[i] = True
                    curr.append(nums[i])
                    recur(curr, size + 1)
                    curr.pop()
                    self.seen[i] = False

        recur([], 0)
        return self.ans