class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(h: List[int]) -> int:
            if not h:
                return 0

            def next_smaller_element(arr):
                n = len(arr)
                res = [0] * n
                stack = [0]
                for i in range(1, n):
                    if arr[i] >= arr[stack[-1]]:
                        stack.append(i)
                    else:
                        while stack and arr[i] < arr[stack[-1]]:
                            res[stack.pop()] = i
                        stack.append(i)
                while stack:
                    res[stack.pop()] = n

                return res

            def previous_smaller_element(arr):
                n = len(arr)
                res = [0] * n
                stack = [n - 1]
                for i in range(n - 1, -1, -1):
                    if arr[i] >= arr[stack[-1]]:
                        stack.append(i)
                    else:
                        while stack and arr[i] < arr[stack[-1]]:
                            res[stack.pop()] = i
                        stack.append(i)
                while stack:
                    res[stack.pop()] = -1

                return res

            nsi = next_smaller_element(h)
            psi = previous_smaller_element(h)

            n = len(h)
            ans = 0

            for i in range(n):
                ans = max(ans, h[i] * (nsi[i] - psi[i] - 1))

            return ans

        if not matrix:
            return 0

        dp = [0] * len(matrix[0])
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[j] = 0
                else:
                    dp[j] += 1

            ans = max(ans, largestRectangleArea(dp))

        return ans