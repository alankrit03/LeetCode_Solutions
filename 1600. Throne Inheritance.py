class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.cache = {kingName: []}
        self.alive = {kingName: True}

    def birth(self, parentName: str, childName: str) -> None:
        self.alive[childName] = True
        if parentName not in self.cache:
            self.cache[parentName] = []
        self.cache[parentName].append(childName)

    def death(self, name: str) -> None:
        self.alive[name] = False

    def getInheritanceOrder(self) -> list[str]:
        order = []

        def DFS(parent):
            if self.alive[parent]:
                order.append(parent)
            if parent not in self.cache:
                return

            for child in self.cache[parent]:
                DFS(child)

        DFS(self.king)
        return order

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()