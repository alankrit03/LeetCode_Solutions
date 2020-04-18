class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return
        max_ = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            arr[i], max_ = max_, max(max_, arr[i])

        arr[-1] = -1
        return arr