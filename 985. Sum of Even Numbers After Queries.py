class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        result = [0] * n

        even_sum = 0
        for x in A:
            if not x % 2:
                even_sum += x

        for i in range(n):
            idx = queries[i][1]
            val = queries[i][0]

            if A[idx] % 2 == 0:
                if val % 2 == 0:
                    even_sum += val
                else:
                    even_sum -= A[idx]

            elif val % 2:
                even_sum += A[idx] + val

            A[idx] += val
            result[i] = even_sum

        return result