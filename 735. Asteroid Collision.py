class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        n = len(asteroids)
        i = 0

        while i < n:
            x = asteroids[i]
            if x > 0:
                ans.append(x)
            else:
                if not ans or ans[-1] < 0:
                    ans.append(x)
                elif abs(x) > ans[-1]:
                    ans.pop()
                    i -= 1
                elif abs(x) == ans[-1]:
                    ans.pop()
            i += 1
        return ans
