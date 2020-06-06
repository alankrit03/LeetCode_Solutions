class Solution:
    def countBits(self, num: int) -> List[int]:
        def numOfBits(x):
            mask = 1
            bits = 0
            while mask <= x:
                if x ^ mask == x - mask:
                    bits += 1
                mask <<= 1

            return bits

        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = numOfBits(i)

        return result