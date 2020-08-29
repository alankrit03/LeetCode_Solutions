class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cache = k * threshold
        n = len(arr)
        ans = 0
        sum_ = sum(arr[:k])

        i, j = 0, k

        if sum_ >= cache:
            ans = 1
        while j < n:
            sum_ -= arr[i]
            sum_ += arr[j]

            if sum_ >= cache:
                ans += 1
            i += 1
            j += 1

        return ans
