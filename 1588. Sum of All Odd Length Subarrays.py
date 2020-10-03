class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            c = ((i + 1) * (n - i) + 1) // 2
            ans += arr[i] * c

        return ans