class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0

        for x in logs:
            if x == './':
                pass
            elif x == '../':
                ans = max(0, ans - 1)
            else:
                ans += 1

        return ans