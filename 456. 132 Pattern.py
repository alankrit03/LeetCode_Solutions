class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_ = [math.inf] * n
        min_[0] = nums[0]
        for i in range(1, n):
            min_[i] = min(min_[i - 1], nums[i])
        # print(min_)

        stack = []
        for i in range(n - 1, -1, -1):
            if nums[i] > min_[i]:
                while stack and stack[-1] <= min_[i]:
                    stack.pop()
                if stack and min_[i] < stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])

        return False