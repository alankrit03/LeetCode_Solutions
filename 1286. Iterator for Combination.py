class CombinationIterator:

    def __init__(self, ch: str, cL: int):
        n = len(ch)
        self.contain = collections.deque()

        def recur(idx, l, st):
            if l == cL:
                self.contain.append(st)
                return
            if idx == n:
                return

            for i in range(idx, n):
                recur(i + 1, l + 1, st + ch[i])

        recur(0, 0, '')

    def next(self) -> str:
        return self.contain.popleft()

    def hasNext(self) -> bool:
        return bool(self.contain)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()