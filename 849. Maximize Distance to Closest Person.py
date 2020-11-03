class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [-1] * n
        start = -1
        for i in range(n):
            if seats[i]:
                start = i
            else:
                left[i] = start

        right = [n] * n
        end = n
        for i in range(n - 1, -1, -1):
            if seats[i]:
                end = i
            else:
                right[i] = end

        ans = 1
        for i in range(n):
            if not seats[i]:
                if left[i] > -1 and right[i] < n:
                    ans = max(ans, min(i - left[i], right[i] - i))
                elif left[i] > -1:
                    ans = max(ans, i - left[i])
                else:
                    ans = max(ans, right[i] - i)

        return ans