class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        queue_idx = collections.deque(range(n))

        ans = [0] * n
        i = 0
        while queue_idx:
            ans[queue_idx.popleft()] = deck[i]
            if queue_idx:
                queue_idx.append(queue_idx.popleft())
            i += 1

        return ans