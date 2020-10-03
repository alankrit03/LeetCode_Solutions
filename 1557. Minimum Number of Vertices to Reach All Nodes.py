class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        cache = set(range(n))

        for u, v in edges:
            if v in cache:
                cache.remove(v)

        return list(cache)
