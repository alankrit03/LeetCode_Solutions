class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        if N < 5:
            return [i for i in range(1, N + 1)]

        graph = [[] for i in range(N)]

        for edge in paths:
            graph[edge[0] - 1].append(edge[1] - 1)
            graph[edge[1] - 1].append(edge[0] - 1)

        ans = [0] * N
        for i in range(4):
            ans[i] = i + 1

        for i in range(4, N):
            color = set()
            adjacent = graph[i]
            # print(adjacent)
            for garden in adjacent:
                color.add(ans[garden])
            for j in range(1, 5):
                if j not in color:
                    ans[i] = j

        return ans