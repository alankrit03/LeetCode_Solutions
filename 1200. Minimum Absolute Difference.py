class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_ = float('inf')
        n = len(arr)

        for i in range(1, n):
            if arr[i] - arr[i - 1] < min_:
                min_ = arr[i] - arr[i - 1]

        result = []

        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_:
                result.append([arr[i - 1], arr[i]])

        return result