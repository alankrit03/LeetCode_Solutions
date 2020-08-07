class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0

        l = len(flowerbed)
        while i < l:
            if not n:
                return True
            if flowerbed[i]:
                i += 2
            else:
                if (i + 1 < l) and (flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    i += 3

        if l == 1:
            if flowerbed[0] == 0:
                n -= 1
        if l > 1:
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                n -= 1
        if n:
            return False
        return True