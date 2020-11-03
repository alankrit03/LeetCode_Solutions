class Solution:
    def distributeCandies(self, candies) -> int:
        c = set(candies)
        n = len(candies)
        return min(n//2,len(c))