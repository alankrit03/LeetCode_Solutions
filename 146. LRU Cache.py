class LRUCache:

    def __init__(self, capacity: int):
        self.n = 0
        self.capacity = capacity
        self.cache = set()
        self.list1 = []

    def get(self, key: int) -> int:
        if key in self.cache:
            for i in range(self.n):
                if self.list1[i][0] == key:
                    if i == self.n - 1:
                        return self.list1[i][1]
                    temp = self.list1.pop(i)
                    self.list1.append(temp)
                    return temp[1]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            for i in range(self.n):
                if self.list1[i][0] == key:
                    if i == self.n - 1:
                        self.list1[i][1] = value
                    else:
                        self.list1.pop(i)
                        self.list1.append([key, value])
        else:
            if self.n < self.capacity:
                self.n += 1
            else:
                self.cache.remove(self.list1.pop(0)[0])

            self.cache.add(key)

            self.list1.append([key, value])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)