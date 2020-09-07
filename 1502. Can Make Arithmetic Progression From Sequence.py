class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        d = arr[1] - arr[0]

        for i in range(1, n):
            if arr[i] - arr[i - 1] != d:
                return False
        return True