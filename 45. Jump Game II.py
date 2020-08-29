class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return 0
        curr = max_ = nums[0]
        jump = 1
        for i in range(n):
            if i>curr:
                jump+=1
                curr = max_
            max_ = max(max_,nums[i]+i)
        return jump