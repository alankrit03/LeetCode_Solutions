class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        visited = [False] * n

        cache = {}
        friend_pref = {}
        for i in range(n):
            x = preferences[i]
            cache[i] = x
            friend_pref[i] = {}
            for j in range(n - 1):
                friend_pref[i][x[j]] = j

        partners = {}
        for x, y in pairs:
            partners[x] = y
            partners[y] = x

        def isUnhappy(curr, partner):
            pref = cache[curr]
            # if
            for x in pref:
                PofX = partners[x]
                if x == partner:
                    break

                if friend_pref[x][curr] < friend_pref[x][PofX]:
                    return True
            return False

        ans = 0
        for x, y in pairs:
            if isUnhappy(x, y):
                ans += 1
            if isUnhappy(y, x):
                ans += 1

        print(friend_pref)

        return ans