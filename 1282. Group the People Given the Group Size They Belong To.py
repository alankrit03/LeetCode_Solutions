class Group:
    def __init__(self):
        self.size = 0
        self.members = []

    def addMember(self, mem):
        self.members.append(mem)
        self.size += 1


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        cache = {}
        ans = []
        n = len(groupSizes)
        for i in range(n):
            x = groupSizes[i]
            if x in cache:
                ob = cache[x]
                if ob.size == x:
                    ans.append(ob.members)
                    cache[x] = Group()
            else:
                cache[x] = Group()

            cache[x].addMember(i)
            if cache[x].size == x:
                ans.append(cache[x].members)
                cache[x] = Group()
        return ans