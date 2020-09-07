class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if t == 0 and len(set(nums)) == n:
            return False

        for i in range(n - 1):
            for j in range(i + 1, min(i + k + 1, n)):
                if abs(nums[j] - nums[i]) <= t:
                    return True

        return False