class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n

        stack = []
        stack.append(0)

        for i in range(1, n):

            if arr[stack[-1]] >= arr[i]:
                stack.append(i)
            else:
                while stack and arr[stack[-1]] < arr[i]:
                    temp = stack.pop()
                    result[temp] = i - temp
                stack.append(i)

        return result