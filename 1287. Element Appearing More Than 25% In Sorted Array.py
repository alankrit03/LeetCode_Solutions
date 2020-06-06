class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        j = -1
        curr = arr[0]
        target = (n // 4) + 1

        while (j - i + 1) < target and j < n - 1:
            if arr[j + 1] == curr:
                j += 1
                continue
            i = j + 1
            curr = arr[i]

        return arr[i]