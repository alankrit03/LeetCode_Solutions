class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []

        def recur(i, idx, arr):
            if idx == k:
                self.ans.append(arr[:])
                return

            if i > n:
                return

            arr[idx] = i
            recur(i + 1, idx + 1, arr)
            recur(i + 1, idx, arr)

        recur(1, 0, [0] * k)

        return self.ans