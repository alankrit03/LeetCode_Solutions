class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n

        for book in bookings:
            ans[book[0] - 1] += book[2]
            if book[1] < n:
                ans[book[1]] -= book[2]

        for i in range(1, n):
            ans[i] += ans[i - 1]

        return ans