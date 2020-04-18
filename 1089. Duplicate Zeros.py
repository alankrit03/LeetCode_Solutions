class Solution:
    from collections import deque
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        que = deque()

        for i in range(n):
            if arr[i] == 0:
                que.append(0)
            if que:
                que.append(arr[i])

                arr[i] = que.popleft()