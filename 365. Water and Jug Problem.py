class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b

            return a

        if not z:
            return True

        return z <= x + y and z % gcd(x, y) == 0