class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        def sortFn(x):

            return x

        if len(votes) == 1:
            return votes[0]
        n = len(votes[0])
        cache = {}

        for x in votes:
            for i in range(n):
                if x[i] not in cache:
                    cache[x[i]] = [0] * n + [x[i]]

                cache[x[i]][i] -= 1

        cache = list(cache.values())
        cache.sort()
        print(cache)
        ans = ''
        for x in cache:
            ans += x[-1]

        return ans