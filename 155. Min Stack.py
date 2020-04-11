class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__min = [10_000_000000]
        self.__stack = []
        self.__count = 0

    def push(self, x: int) -> None:
        self.__stack.append(x)
        self.__count += 1
        if x <= self.__min[-1]:
            self.__min.append(x)

    def pop(self) -> None:
        if self.__count:
            temp = self.__stack.pop()
            self.__count -= 1
            if temp == self.__min[-1]:
                self.__min.pop()

    def top(self) -> int:
        if self.__count:
            return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()