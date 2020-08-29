class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total = prev = 0
        for i in range(len(arr)):
            if arr[i] & 1:
                total += i + 1 - prev
                prev = i + 1 - prev
            else:
                total += prev

        return total % (10e9+7)