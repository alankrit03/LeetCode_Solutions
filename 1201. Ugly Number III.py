class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(num1, num2):
            def gcd(num1, num2):
                while (num2 != 0):  # When num2 is not equal to 0
                    # Swap num2 with num1 using temp
                    num1, num2 = num2, num1 % num2
                return num1

            return (num1 * num2) // gcd(num1, num2)  # LCM is found using GCD

        def ispossible(x):
            count = x // a + x // b + x // c
            count -= (x // ab + x // bc + x // ac)

            count += x // abc

            if count >= n:
                return True
            return False

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(a, bc)
        lo = 1
        hi = b * n

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if ispossible(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
