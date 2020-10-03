class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        def build(st, cache):
            word = ''
            st = st.strip()
            for x in st:
                if x == ' ':
                    try:
                        cache[word] += 1
                    except:
                        cache[word] = 1
                    finally:
                        word = ''
                else:
                    word += x
            else:
                try:
                    cache[word] += 1
                except:
                    cache[word] = 1

            return cache

        cacheA = build(A, {})
        cacheB = build(B, {})
        # print(cacheA)
        # print(cacheB)
        ans = []
        for x, y in cacheA.items():
            if y == 1:
                if x not in cacheB:
                    ans.append(x)

        for x, y in cacheB.items():
            if y == 1:
                if x not in cacheA:
                    ans.append(x)

        return ans