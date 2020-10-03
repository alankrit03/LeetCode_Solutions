class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []

        def recur(ele, sum_, idx, temp):
            if ele == k and sum_ == 0:
                self.ans.append(temp[:])
            if sum_ < 1:
                return

            for i in range(idx, 10):
                temp.append(i)
                recur(ele + 1, sum_ - i, i + 1, temp)
                temp.pop()

        recur(0, n, 1, [])

        return self.ans