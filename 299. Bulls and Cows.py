class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cache1 = {}
        cache2 = {}
        a = 0
        b = 0

        for i in range(len(secret)):
            x = secret[i]
            y = guess[i]
            if x == y:
                a += 1
                continue
            # print('cache1',cache1,cache1.get(y))
            if cache1.get(y, 0) > 0:
                b += 1
                cache1[y] -= 1
            else:
                try:
                    cache2[y] += 1
                except:
                    cache2[y] = 1

            if cache2.get(x, 0) > 0:
                b += 1
                cache2[x] -= 1
            else:
                try:
                    cache1[x] += 1
                except:
                    cache1[x] = 1
            # print(cache1)
            # print(cache2)

        return str(a) + 'A' + str(b) + 'B'