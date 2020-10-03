class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        cache1 = set('qwertyuiopQWERTYUIOP')
        cache2 = set('asdfghjklASDFGHJKL')
        cache3 = set('zxcvbnmZXCVBNM')

        def func(cache, word):
            for x in word:
                if x not in cache:
                    return False

            return True

        ans = []
        for x in words:
            flag = False
            if x[0] in cache1:
                flag = func(cache1, x)
            elif x[0] in cache2:
                flag = func(cache2, x)
            else:
                flag = func(cache3, x)

            if flag:
                ans.append(x)

        return ans