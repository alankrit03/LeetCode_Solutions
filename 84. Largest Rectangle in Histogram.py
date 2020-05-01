class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
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
