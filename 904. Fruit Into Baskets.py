class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0

        n = len(tree)
        ans = 0

        first = tree[0]
        firstidx = 0

        second = None
        prev = 0

        for i in range(1, n):
            x = tree[i]
            if x != first:
                if second is None:
                    second = x
                if second != x:
                    ans = max(ans, i - firstidx)
                    firstidx = prev
                    first = tree[prev]
                    second = x

            if x != tree[i - 1]:
                prev = i
        # print(ans,n,firstidx)
        ans = max(ans, n - firstidx)
        return ans
