"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
This question irritated me more than any other algorithmic problem in recent times.
Example 1:

Input: [5,7]
Output: 4
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if not m:
            return 0

        if n - m < 2:
            return m & n

        power = 1
        while power <= n:
            if m < power <= n:
                return 0
            power *= 2

        power //= 2
        ans = 0
        temp = m

        while power >= n - m + 1:
            if temp >= power and power & m and power & n:
                ans += power
                temp = temp - power
            power //= 2

        return ans