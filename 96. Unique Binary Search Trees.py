class Solution:
    def numTrees(self, n: int) -> int:
        self.cache = {0: 1, 1: 1}

        def recur(nodes):
            if nodes in self.cache:
                return self.cache[nodes]
            total = 0
            for i in range(nodes):
                l = recur(i)
                r = recur(nodes - i - 1)
                total += (l * r)

            self.cache[nodes] = total
            return total

        ans = recur(n)

        return ans