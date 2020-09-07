class Solution:
    def largestTimeFromDigits(self, nums: List[int]) -> str:
        def isValid(time):
            hr = int(time[:2])
            m = int(time[2:])
            if hr >= 24:
                return False
            if m > 59:
                return False
            return True

        n = 4
        for i in range(n):
            nums[i] = str(nums[i])
        self.seen = [False] * n
        self.ans = ''

        def recur(curr, size):
            if size == n:
                temp = ''.join(curr)
                if isValid(temp):
                    try:
                        if temp[:2] + ':' + temp[2:] > self.ans:
                            self.ans = temp[:2] + ':' + temp[2:]
                    except:
                        self.ans = temp[:2] + ':' + temp[2:]
                return

            for i in range(n):
                if not self.seen[i]:
                    self.seen[i] = True
                    curr.append(nums[i])
                    recur(curr, size + 1)
                    curr.pop()
                    self.seen[i] = False

        recur([], 0)
        return self.ans